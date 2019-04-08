import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
import nibabel as nib

metric = ['ad', 'ak', 'awf', 'eas_De_par', 'eas_De_perp', 'eas_tort', 'FA', 'ias_Da', 'md', 'mk', 'rd', 'rk']
mask_name = ['1_L_thal','2_R_thal','CC_Body_mask','CC_Genu_mask','CC_Splenium_mask']


def get_subject_data(index, dict):
	'''
	for an index get an image unshffuled!
	'''
	assert (index > -1) and (index < 166)

	if index < 67:
		# positive of 117
		pass
	elif (index > 66) and (index < 117):
		# negative of 117
		pass
	else:
		# old subjects
		pass

def show_slice(data, N):
	'''
	data: 3d ndarray
	N: number of slice taken at X axis
	'''
	slices = np.round (np.linspace (0, data.shape[0], N, endpoint=False)).astype(np.int16)
	fig, ax = plt.subplots(1, N, figsize=(15, 4), sharey=True)

	for i,s in enumerate(slices):
		ax[i].imshow(data[s], cmap='gray')

def get_image(index, metric, positive, verbose=False):
	'''
	get negative sample of 117 data
	'''
	M = len(metric)
	data_metric = np.zeros([M, 182, 218, 182])

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
	data_metric = np.zeros([M, 182, 218, 182])

	for i, m in enumerate(metric):
		PATH = './data/prior_cycle_subj_all_DKI_metrics/mat/'+m+'_priorsubj'+'{:02}'.format(index+1)+'.mat'
		data_metric[i] = loadmat(PATH)['vol']

		if verbose:
			show_slice(data_metric[i], N=8)

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
	filename = img_name + '.nii'
	array_img = nib.Nifti1Image(img, np.eye(4))
	nib.save(array_img, filename)

	pass