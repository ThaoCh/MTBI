import torch
import numpy as np
from torch.utils.data import Dataset
from scipy.ndimage import affine_transform
from datautility import *

def toTensor (sample):
	'''
	Notes:
		Mean Reduction on image, OneHot on label, Convert one sample to single tensor
	Args:
		sample: dict of ndarray, image in [0, 255], (C=1, X, Y, Z), 
			label in {0, 0.5, 1}, (C=1, X, Y, Z)
		device: torch.device('cuda')/torch.device('cpu')
	Ret:
		Dict of:
			imageTensor range [0, 255] with mean 0, (C=1, X, Y, X)
			labelTensor in [0, 1], (C=3, X, Y, X)
	'''
	image, label = sample['image'], sample['label']
	image -= 0.5 # normalize
	imageTensor = torch.from_numpy(image.copy()) # copy from memory to avoid minus stride
	labelTensor = torch.from_numpy(label.copy())

	return {'image': imageTensor, 'label': labelTensor}

def AffineFun(img, xr, yr, zr, xm, ym, zm, order):
	'''
	Notes:
		Rotate and move
		MoveToCenter->RotateX->RotateY->RotateZ->MoveBack->MoveRandom
	Args:
		img: image of shape (C, X, Y, Z)
		xr, yr, zr: Rotate in degree
		xm, ym, zm: move as int
		order: 3 for image, 0 for label
	Ret:
		img: Transformed image of shape (C, X, Y, Z)
	'''
	sinx = np.sin(np.deg2rad(xr))
	cosx = np.cos(np.deg2rad(xr))

	siny = np.sin(np.deg2rad(yr))
	cosy = np.cos(np.deg2rad(yr))

	sinz = np.sin(np.deg2rad(zr))
	cosz = np.cos(np.deg2rad(zr))

	xc = img[0].shape[0]//2
	yc = img[0].shape[1]//2
	zc = img[0].shape[2]//2

	Mc = np.array([[1, 0, 0, xc],[0, 1, 0, yc],[0, 0, 1, zc],[0, 0, 0, 1]])
	Rx = np.array([[cosx, sinx, 0, 1],[-sinx, cosx, 0, 1],[0, 0, 1, 1], [0, 0, 0, 1]])
	Ry = np.array([[cosy, 0, siny, 1],[0, 1, 0, 1],[-siny, 0, cosy, 1], [0, 0, 0, 1]])
	Rz = np.array([[1, 0, 0, 1],[0, cosz, sinz, 1],[0, -sinz, cosz, 1], [0, 0, 0, 1]])
	Mb = np.array([[1, 0, 0, -xc],[0, 1, 0, -yc],[0, 0, 1, -zc],[0, 0, 0, 1]])
	MM = np.array([[1, 0, 0, xm],[0, 1, 0, ym],[0, 0, 1, zm],[0 ,0, 0, 1]])

	Matrix = np.linalg.multi_dot([Mc, Rx, Ry, Rz, Mb, MM])

	C = img.shape[0]
	for chan in np.arange(C):
		img[chan] = affine_transform(img[chan], Matrix, output_shape=img[chan].shape, order=order)

	return img

def filpFun(img, x, y, z):
	'''
	Notes:
		filp image
	Args:
		img: image of shape (C, X, Y, Z)
		x, y, z: filp x ? filp y ? flip z ?
	Ret:
		img: Transformed image of shape (C, X, Y, Z)
	'''
	if x==True:
		img = np.flip(img, axis=1)

	if y==True:
		img = np.flip(img, axis=2)

	if z==True:
		img = np.flip(img, axis=3)

	return img

def downSampleFun(img, level, order):
	'''
	Args:
		img: shape [1, X, Y, Z]
		level: scaling factor of downsampling
		order: 3 for image, 0 for label
	Ret:
		imgout: down sampled image of shape [1, X//level, Y//level, Z//level]
	'''
	if level == 1:
		return img
	else:
		C, x, y, z = img.shape

		imgout = np.zeros([C, x//level, y//level, z//level], dtype=np.float32)
		Matrix = np.array([[level, 0, 0, 0],[0, level, 0, 0],[0, 0, level, 0],[0, 0, 0, 1]])
		for chan in np.arange(C):
			imgout[chan] = affine_transform(img[chan], Matrix, output_shape=imgout[chan].shape, order=order)
		return imgout

class downSample(object):
	'''
	Down sample happens before affine
	'''
	def __init__(self, level):

		self.level = level
		pass

	def __call__(self, sample):

		image, label = sample['image'], sample['label']
		return {'image': downSampleFun(image, self.level, 3), \
				'label': label}

class RandomFilp(object):
	def __init__(self, p):
		self.p = p

	def __call__(self, sample):
		x, y, z = np.random.uniform(0, 1, size=3)
		p = self.p
		image, label = sample['image'], sample['label']
		return {'image': filpFun(image, (x<p), (y<p), (z<p)), \
			'label': label}

class RandomAffine(object):
	'''
	Random rotation and move
	'''
	def __init__(self, fluR, fluM):

		self.fluR = fluR
		self.fluM = fluM

	def __call__(self, sample):

		xr, yr, zr = np.random.uniform(-self.fluR, self.fluR, size=3)		
		xm, ym, zm = np.random.uniform(-self.fluM, self.fluM, size=3)

		image, label = sample['image'], sample['label']
		return {'image': AffineFun(image, xr, yr, zr, xm, ym, zm, 3), \
				'label': label}

class MTBIDatasetSub(Dataset):
	'''
	pytorch dataset for bv segmentation
	'''
	def __init__(self, new_index, shuffle_index, metric, transform=None):
		'''
		Args:
			index of int
			No Conversion of anykind in a dataset class!
			transform(callable, default=none): transfrom on a sample
		'''
		self.new_index = new_index
		self.shuffle_index = shuffle_index
		self.metric = metric
		self.transform = transform

	def __len__(self):
		'''
		Override: return size of dataset
		'''
		return len(self.new_index)

	def __getitem__(self, indice):
		'''
		Override: integer indexing in range from 0 to len(self) exclusive.
		type: keep as np array
		'''

		name = self.new_index[indice] # Hummm complicated
		# image = np.zeros([8,96,96,96])
		image = get_image_subject(name, self.metric, 'new', shape=(96, 96, 96), verbose=False)

		if name[2] == 'I':
			# Positive
			label = np.array([1])
		
		else:
			# Negative
			label = np.array([0])
		
		sample = {'image':image, 'label':label}

		if self.transform:
			sample = self.transform(sample)

		sample = toTensor(sample)

		return sample

class MTBIDataset(Dataset):
	'''
	pytorch dataset for bv segmentation
	'''
	def __init__(self, shuffle_idx, img_dict, metric, transform=None, mode='new'):
		'''
		Args:
			index of int
			No Conversion of anykind in a dataset class!
			transform(callable, default=none): transfrom on a sample
		'''
		self.shuffle_idx = shuffle_idx
		self.img_dict=img_dict
		self.metric = metric	
		self.transform=transform
		self.mode = mode

	def __len__(self):
		'''
		Override: return size of dataset
		'''
		return (self.img_dict).shape[0]

	def __getitem__(self, indice):
		'''
		Override: integer indexing in range from 0 to len(self) exclusive.
		type: keep as np array
		'''
		indice = self.shuffle_idx[indice]

		if self.mode=='new':
			image = get_subject_data_new(indice, self.img_dict, self.metric, shape=(64, 96, 64), verbose=False)
			label = get_label_new(indice)
		else:
			# mode == all
			image = get_subject_data_all(indice, self.img_dict, self.metric, shape=(64, 96, 64), verbose=False)
			label = get_label_all(indice)

		sample = {'image':image, 'label':label}

		if self.transform:
			sample = self.transform(sample)

		sample = toTensor(sample)

		return sample


