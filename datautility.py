import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import nibabel as nib

def get_label_new(index):

	assert (index < 117) and (index > -1) 

	if index < 67:
		return np.array ([1])
	else:
		return np.array ([0])

def get_label_all(index):

	assert (index > -1) and (index < 154)

	if index < 27:
		return np.array ([1])
	elif index < 49:
		return np.array ([0])
	elif index < 106:
		return np.array ([1])
	else:
		return np.array ([0])

def zero_padding (img, target_x, target_y, target_z):
	"""
	reshaping the img to desirable shape through zero pad or crop
	Args:
		* img: input ndarray (C, X, Y, Z)
		* target_x: target shape x
		* target_y: target shape y
		* target_z: target shape z
	Ret:
		img: reshaped 3d nii array
	"""

	C = img.shape[0]

	padx = (target_x-img.shape[1])//2
	pady = (target_y-img.shape[2])//2
	padz = (target_z-img.shape[3])//2

	img_ret = np.zeros((C, target_x, target_y, target_z), dtype=np.float32)

	for chan in np.arange(C):

		if padx<0:
			temp = img[chan,-padx:padx,:,:]
		else:
			temp = np.pad (img[chan], ((padx,padx),(0, 0),(0, 0)), \
				mode='constant', constant_values=((0,0),(0,0),(0,0)))

		if pady <0:
			temp = temp[:,-pady:pady,:]
		else:
			temp = np.pad (temp, ((0,0),(pady, pady),(0, 0)), \
				mode='constant', constant_values=((0,0),(0,0),(0,0)))

		if padz <0:
			temp = temp[:,:,-padz:padz]
		else:
			temp = np.pad (temp, ((0,0),(0, 0),(padz, padz)), \
				mode='constant', constant_values=((0,0),(0,0),(0,0)))
		img_ret[chan] = temp
	return img_ret	

def get_subject_data_new(index, image_dict, metric, shape, verbose=False):
	'''
	for an index get an image
	index: [0-117]
	'''

	assert (index < 117) and (index > -1) 

	if index < 67:
		# positive
		data = get_image (image_dict[index], metric, positive=True, verbose=verbose)
	else:
		# index => 67 < 117, negative	
		data = get_image (image_dict[index], metric, positive=False, verbose=verbose)

	return zero_padding (data, *shape)

def get_subject_data_all(index, image_dict, metric, verbose=False):
	'''
	for an index get an image unshffuled!
	Args:
		index: the index of image in image_dict in range [0, 154)
		image_dict: the dict of image names
		metric: the metric to obtain
		verbose: print image out or not
	Return:
		data: ndarray, shape = (len(metric), X, Y, Z)
	'''
	assert (index > -1) and (index < 154)

	if index < 49:
		# 49 old subjects
		data = get_old_image (image_dict[index], metric, verbose=verbose)
	elif (index < 106):
		# 57 positive of 117
		data = get_image (image_dict[index], metric, positive=True, verbose=verbose)
	else:
		# 48 negative of 117
		data = get_image (image_dict[index], metric, positive=False, verbose=verbose)

	return zero_padding (data, *shape)

def show_slice(data, N, axis=0):
	'''
	data: 3d ndarray
	N: number of slice taken at X axis
	'''
	slices = np.round (np.linspace (0, data.shape[0], N, endpoint=False)).astype(np.int16)
	fig, ax = plt.subplots(1, N, figsize=(15, 4), sharey=True)

	for i,s in enumerate(slices):
		if axis==0:
			ax[i].imshow(data[s], cmap='gray')
		elif axis==1:
			ax[i].imshow(data[:,s,:], cmap='gray')
		else:
			ax[i].imshow(data[:,:,s], cmap='gray')
	pass

def get_image(index, metric, positive, verbose=False):
	'''
	get sample of 117 data
	'''
	M = len(metric)
	data_metric = np.zeros([M, 182, 218, 182], dtype=np.float32)

	for i, m in enumerate(metric):
		if positive:
			PATH = './data/current_cycle_117subj_all_metrics/mat/'+m+'_TBI'+'{:03}'.format(index)+'.mat'
		else:
			# negative
			if (index==13) or (index==14):
				# 13, 14 is broken
				PATH = './data/current_cycle_117subj_all_metrics/mat/'+m+'_TBN'+'{:03}'.format(index)+'_2'+'.mat'
			else:
				PATH = './data/current_cycle_117subj_all_metrics/mat/'+m+'_TBN'+'{:03}'.format(index)+'.mat'

		data_metric[i] = loadmat(PATH)['vol']

		if verbose:
			show_slice(data_metric[i], N=8)
	return data_metric

def get_old_image(index, metric, verbose=False):
	M = len(metric)
	data_metric = np.zeros([M, 182, 218, 182], dtype=np.float32)

	for i, m in enumerate(metric):
		# special, need a +1 to correspond to the correct file
		PATH = './data/prior_cycle_subj_all_DKI_metrics/mat/'+m+'_priorsubj'+'{:02}'.format(index+1)+'.mat'
		data_metric[i] = loadmat(PATH)['vol']

		if verbose:
			show_slice(data_metric[i], N=8)
			pass
	return data_metric

def get_mask(mask, verbose=False):
	
	M = len(mask)

	mask_array = np.zeros([M, 182, 218, 182])
	for i, m in enumerate(mask):
		PATH = './data/masks/' + m + '.mat'
		mask_array[i] = loadmat(PATH)['vol']

		if verbose:
			show_slice(mask_array[i], N=8)
	return mask_array

def savenii(img, img_name): 
	'''
	Saving the mask to nii file in format
	Args:
		* img: ndarray of shape (X, Y, Z) quantized
		* img_name: str of image index
	return:
		* None
	'''
	img = np.squeeze(img)
	filename = img_name + '.nii'
	array_img = nib.Nifti1Image(img, np.eye(4))
	nib.save(array_img, filename)

	pass