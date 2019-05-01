import os
import datetime

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from scipy.ndimage import affine_transform, zoom
from tqdm import tqdm

image_path = 'bv_body_data/predict/'
data_path = 'img_'
label_path = 'bv_body'
appendix_str = '.nii'

def loadnii(x, xout=-1, yout=-1, zout=-1, mode='pad'):

	"""
	load the nii image and label into np array 
	input:
		x: int index of the image to read
	return: 
		tuple of (image, label)
	"""

	data_file = os.path.join(image_path, data_path + str(x) + appendix_str)
	label_file = os.path.join(image_path, label_path + str(x)+ appendix_str)

	data = ((nib.load(data_file)).get_fdata()).astype(np.float32)
	label = ((nib.load(label_file)).get_fdata()).astype(np.float32)/2

	if xout < 0:
		data = data.reshape(1, *data.shape)
		label= label.reshape(1, *label.shape)

		return (data, label) # perserve original image shape
	
	else:

		if mode == 'pad':
			data = zero_padding(data, xout, yout, zout)
			label = zero_padding(label, xout, yout, zout)

		else:
			x, y, z = data.shape
			#scale the image
			data = zoom(data, zoom=(xout/x, yout/y, zout/z))
			label = zoom(label, zoom=(xout/x, yout/y, zout/z))

		data = data.reshape(1, *data.shape)
		label= label.reshape(1, *label.shape)

		return (data, label)

def findBV(n):
	'''
	Find BV for single image of shape [1, X, Y, Z] and channel [1, X, Y, Z]
	'''
	
	stride = 8

	dict = {}

	data, label = loadnii(n) # load the original image
	label = (label > 0.66).astype(np.float32)

	_, h, w, d = data.shape
	x, y, z = 0, 0, 0

	bv = np.sum(label)

	while x < h-127:
		y = 0
		while y < w-127:
			z = 0
			while z < d-127:
				datanew = data[0:1, x:x+128, y:y+128, z:z+128]
				labelnew = label[0:1, x:x+128, y:y+128, z:z+128]
				bvnew = np.sum(labelnew)

				if bvnew > bv*0.95:
					dict[(n, x, y, z)] = 1
				elif bvnew < bv*0.6:
					dict[(n, x, y, z)] = 0
				else:
					pass

				z += stride
			y += stride
		x += stride 

	# code for debugging
	# v = list (dict.values())
	# print('image {0} generate {1} samples, with positive rate = {2:.4f}'.format (n, len(v), np.sum(v)/len(v)))

	return dict


def generateSW(nlist):
	dict = {}
	for n in tqdm (nlist):
		dictTemp = findBV(n)
		dict.update(dictTemp)
		v = list (dict.values())
	print (' In total generate {0} samples, with overall positive rate = {1:.4f}'.format (len(v), np.sum(v)/len(v)))

	return dict

def savenii(img, img_name): 
	'''
	Saving the mask to nii file in format
	Args:
		* img: ndarray of shape (1, X, Y, Z) quantized
		* img_name: str of image index
	return:
		* None
	'''
	timestamp = datetime.datetime.now()
	filename = img_name + '-' + str(timestamp) + appendix_str
	array_img = nib.Nifti1Image(img, np.eye(4))
	nib.save(array_img, filename)

	pass

def getniishape(x):
	"""
	Get the shape of an image
	input:
		* x: int of image index
	return: 
		* tuple (X, Y, X)
	"""
	label_file = os.path.join(image_path, label_path + str(x)+ appendix_str)
	label = ((nib.load(label_file)).get_fdata()).astype(np.float32)/2

	return label.shape

def zero_padding (img, target_x, target_y, target_z):
	"""
	reshaping the img to desirable shape through zero pad or crop
	Args:
		* img: input 3d nii array
		* target_x: target shape x
		* target_y: target shape y
		* target_z: target shape z
	Ret:
		img: reshaped 3d nii array
	"""

	padx = (target_x-img.shape[0])//2
	pady = (target_y-img.shape[1])//2
	padz = (target_z-img.shape[2])//2

	if padx<0:
		img = img[-padx:padx,:,:]
	else:
		img = np.pad (img, ((padx,padx),(0, 0),(0, 0)), \
			mode='constant', constant_values=((0,0),(0,0),(0,0)))

	if pady <0:
		img = img[:,-pady:pady,:]
	else:
		img = np.pad (img, ((0,0),(pady, pady),(0, 0)), \
			mode='constant', constant_values=((0,0),(0,0),(0,0)))

	if padz <0:
		img = img[:,:,-padz:padz]
	else:
		img = np.pad (img, ((0,0),(0, 0),(padz, padz)), \
			mode='constant', constant_values=((0,0),(0,0),(0,0)))

	return img	


def show_image(img, label, indice=-1):
	"""
	show a slice of image with label at certain indice
	Args:
		* img: input image (1, X, Y, Z)
		* label: input label after one hot coding (C, X, Y, Z)
		* indice: cutting indice
	Ret: 
		* None
	"""
	if indice ==-1:
		indice = img.shape[1]//2

	N = label.shape[0]
	fig, ax = plt.subplots(1, N+1, figsize=(12, 4), sharey=True)
	ax[0].imshow(img[0][indice], cmap='gray')
	# have to show the original image

	for i in range(N):
		ax[i+1].imshow(label[i][indice], cmap='gray')
	plt.show()

	pass

def show_batch_image(img, label, batchsize, indice=-1):
	'''
	show batch of Tensor as image

	'''
	img = img.numpy()
	label = label.numpy()

	for i in range(batchsize):
		show_image(img[i], label[i], indice)

	pass


def loadallnii(x, bad_index, target_x=-1, target_y=-1, target_z=-1, verbose=False):

	"""
	DEP!
	load all nii image and label into np array
	input:
		x: number of image
		traget_shape: if preknown the target shape, else calculate
		verbose: whether print the slicing out
	return: 
		tuple of array (max x, max y, max z)
	"""

	target_shape = None

	if target_x < 0:
		target_shape = getniishape(x)
	else:
		target_shape = (target_x, target_y, target_z)

	xx = x - bad_index.shape[0]

	image = np.zeros((xx, 1, *target_shape), dtype=np.float32) # single channel image
	label = np.zeros((xx, 1, *target_shape), dtype=np.float32) # triple channel label

	j = 0
	for i in range(x):

		if np.isin(i, bad_index):
			pass
		else:
			temp_image, temp_label = loadnii(i, target_x, target_y, target_z)
			current_shape = temp_image.shape
			padx = (target_shape[0]-current_shape[0])//2

			image[j] = zero_padding(temp_image, *target_shape)
			label[j] = zero_padding(temp_label, *target_shape)/2

			print('image index loaded: ' + str(i))

			if verbose:
				show_image(image[j], label[j] , 90+padx)

			else:
				pass

			j += 1

	return (image, label)

