# Negative - T1 Letter Number

* from 10 valid feature to 20 valid features, 11 of them are new statistics
* 1st iter grid search hyperparameter using less than 10 feature, 2nd iter expand to all valid feature number

* 1st iter: 
	* maximum test accuracy= 0.400, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.000, 0.002, 0.050) from 14 metrics
	* ['3m-CC_Splenium_mask-ad' 'mean-CC_Splenium_mask-eas_tort'
	 '3m-CC_Splenium_mask-rk' 'kut-1_L_thal-eas_tort' 'mean-1_L_thal-rd'
	 'std-CC_Splenium_mask-eas_De_par' '3m-2_R_thal-eas_tort'
	 'std-CC_Splenium_mask-ak' '4m-CC_Body_mask-rk' '2m-CC_Body_mask-eas_tort']

* 2nd iter:
	* maximum test accuracy= 0.502, achieved by using 20 features and ( C, Gamma, eps)= ( 1000.000, 0.002, 0.050) from 14 metrics
	* ['3m-CC_Splenium_mask-ad' 'mean-CC_Splenium_mask-eas_tort'
	 '3m-CC_Splenium_mask-rk' 'kut-1_L_thal-eas_tort' 'mean-1_L_thal-rd'
	 'std-CC_Splenium_mask-eas_De_par' '3m-2_R_thal-eas_tort'
	 'mean-2_R_thal-ias_Da' '4m-CC_Body_mask-rk' '2m-CC_Body_mask-eas_tort'
	 'std-2_R_thal-eas_tort' 'mean-CC_Genu_mask-rk' '3m-CC_Splenium_mask-FA'
	 '3m-CC_Splenium_mask-ias_Da' 'kut-CC_Splenium_mask-eas_De_par'
	 'std-CC_Splenium_mask-eas_De_perp' 'kut-CC_Genu_mask-ak'
	 'std-CC_Splenium_mask-ak' 'kut-2_R_thal-md' '3m-CC_Splenium_mask-md

# Negative - Digit Span Forward T1

* 1st iter:
	* maximum test accuracy= 0.300, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.10000) from 14 metrics
	['kut-CC_Genu_mask-eas_tort' '2m-CC_Body_mask-eas_tort'
	 'kut-CC_Splenium_mask-rd' 'std-CC_Genu_mask-FA'
	 '4m-CC_Body_mask-eas_tort' 'mean-CC_Splenium_mask-eas_tort'
	 'kut-CC_Body_mask-rk' '3m-2_R_thal-rk' 'mean-CC_Genu_mask-eas_tort'
	 'kut-2_R_thal-ias_Da']

* 2nd iter:
	* maximum test accuracy= 0.404, achieved by using 58 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.10000) from 14 metrics
	* ['kut-CC_Genu_mask-eas_tort' '2m-CC_Body_mask-eas_tort'
	 'kut-CC_Splenium_mask-rd' 'std-CC_Genu_mask-FA'
	 '4m-CC_Body_mask-eas_tort' 'mean-CC_Splenium_mask-eas_tort'
	 'kut-CC_Body_mask-rk' '3m-2_R_thal-rk' 'mean-CC_Genu_mask-eas_tort'
	 'kut-2_R_thal-ias_Da' 'mean-2_R_thal-ak' 'std-CC_Splenium_mask-rd'
	 'std-CC_Splenium_mask-FA' 'mean-2_R_thal-awf'
	 'kut-CC_Splenium_mask-ias_Da' '4m-CC_Genu_mask-ias_Da'
	 'kut-CC_Genu_mask-ak' 'std-1_L_thal-ak' '4m-CC_Genu_mask-ak'
	 '3m-CC_Genu_mask-ias_Da' '3m-CC_Body_mask-md' '4m-CC_Body_mask-ias_Da'
	 'kut-CC_Splenium_mask-mk' 'mean-CC_Body_mask-ak' '3m-CC_Body_mask-rd'
	 'std-CC_Splenium_mask-md' '4m-2_R_thal-awf' 'std-CC_Genu_mask-md'
	 '3m-CC_Body_mask-ias_Da' 'mean-CC_Genu_mask-FA'
	 'kut-CC_Splenium_mask-awf' 'kut-CC_Genu_mask-ias_Da'
	 'std-CC_Splenium_mask-ias_Da' 'kut-CC_Body_mask-ias_Da'
	 '2m-CC_Genu_mask-ak' '3m-CC_Body_mask-mk' 'kut-CC_Body_mask-eas_De_perp'
	 'std-1_L_thal-ias_Da' '2m-CC_Genu_mask-awf' '3m-1_L_thal-ias_Da'
	 '2m-CC_Body_mask-md' '4m-CC_Genu_mask-md' 'kut-CC_Body_mask-md'
	 '2m-CC_Body_mask-mk' '2m-CC_Body_mask-rd' '4m-CC_Genu_mask-awf'
	 '4m-CC_Genu_mask-eas_De_par' '3m-2_R_thal-eas_De_par'
	 'std-CC_Body_mask-eas_De_par' 'std-1_L_thal-eas_De_par' 'std-1_L_thal-rd'
	 '3m-1_L_thal-mk' '3m-1_L_thal-eas_De_par' 'std-1_L_thal-mk'
	 'std-1_L_thal-eas_De_perp' '3m-1_L_thal-rd' '3m-1_L_thal-eas_De_perp'
	 'mean-CC_Genu_mask-mk']

# Negative - Digit Span Backward T1
* imporvement in R2 score from __0.33 -> 0.552__ provided in alp's report
* 1st iter:
	* maximum test accuracy= 0.452, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.10000) from 14 metrics
	* Selected feature for 3xiter= [216. 107. 165. 358. 149.  71. 359.  41.  53. 319.]
	* ['3m-CC_Genu_mask-ad' 'std-CC_Genu_mask-rk' '2m-CC_Genu_mask-mk'
	 'kut-CC_Splenium_mask-rd' '2m-CC_Body_mask-eas_tort' 'std-1_L_thal-rk'
	 'kut-CC_Splenium_mask-rk' 'mean-CC_Genu_mask-eas_tort'
	 'mean-CC_Splenium_mask-eas_tort' 'kut-2_R_thal-ias_Da']
	total time= 2997.831740140915

* 2nd iter:
	* maximum test accuracy= 0.552, achieved by using 59 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.10000) from 14 metrics
	* ['3m-CC_Genu_mask-ad' 'std-CC_Genu_mask-rk' '2m-CC_Genu_mask-mk'
	 'kut-CC_Splenium_mask-rd' '2m-CC_Body_mask-eas_tort' 'std-1_L_thal-rk'
	 'kut-CC_Splenium_mask-rk' 'mean-CC_Genu_mask-eas_tort'
	 'mean-CC_Splenium_mask-eas_tort' 'kut-2_R_thal-ias_Da'
	 'mean-CC_Body_mask-eas_tort' '3m-CC_Genu_mask-FA' '4m-CC_Body_mask-rk'
	 '2m-CC_Splenium_mask-eas_tort' 'std-CC_Genu_mask-FA' '3m-CC_Body_mask-FA'
	 '2m-2_R_thal-FA' 'mean-CC_Splenium_mask-ias_Da' '3m-1_L_thal-ad'
	 'kut-CC_Body_mask-ias_Da' '3m-CC_Splenium_mask-mk' 'mean-CC_Body_mask-md'
	 'kut-CC_Genu_mask-eas_De_par' 'std-1_L_thal-FA' 'kut-CC_Body_mask-md'
	 'mean-CC_Splenium_mask-md' '3m-1_L_thal-awf' '3m-CC_Genu_mask-mk'
	 '3m-2_R_thal-ak' 'std-2_R_thal-mk' '3m-1_L_thal-eas_De_par'
	 'std-1_L_thal-md' '3m-1_L_thal-rd' 'std-1_L_thal-rd'
	 'std-1_L_thal-eas_De_perp' '3m-1_L_thal-eas_De_perp' '3m-1_L_thal-mk'
	 'std-1_L_thal-eas_De_par' 'std-2_R_thal-eas_De_perp'
	 'std-CC_Body_mask-eas_De_perp' '4m-CC_Body_mask-mk' '4m-CC_Body_mask-rd'
	 'std-1_L_thal-mk' 'std-CC_Body_mask-eas_De_par' 'std-2_R_thal-eas_De_par'
	 '4m-CC_Genu_mask-eas_De_par' 'mean-CC_Splenium_mask-eas_De_par'
	 '2m-CC_Body_mask-mk' 'kut-CC_Genu_mask-eas_De_perp'
	 'mean-CC_Genu_mask-eas_De_par' '3m-2_R_thal-eas_De_perp' '3m-2_R_thal-mk'
	 'std-2_R_thal-awf' '4m-CC_Genu_mask-eas_De_perp' '3m-2_R_thal-awf'
	 'mean-CC_Body_mask-rd' 'kut-CC_Body_mask-rd' 'std-2_R_thal-rd'
	 '4m-CC_Genu_mask-rd']

# Combine - T1 Letter Number
# Combine - Digit Span Forward T1
# Combine - Digit Span Backward T1

maximum test accuracy= 0.323, achieved by using 10 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.50000) from 14 metrics
['3m-CC_Body_mask-FA' '3m-CC_Body_mask-eas_tort' 'std-CC_Genu_mask-md'
 'std-CC_Genu_mask-mk' '2m-CC_Splenium_mask-FA' '2m-CC_Body_mask-eas_tort'
 'kut-CC_Splenium_mask-mk' 'kut-CC_Splenium_mask-ak' '2m-2_R_thal-ias_Da'
 'kut-2_R_thal-FA']

 maximum test accuracy= 0.368, achieved by using 30 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.50000) from 14 metrics
['3m-CC_Body_mask-FA' '3m-CC_Body_mask-eas_tort' 'std-CC_Genu_mask-md'
 'std-CC_Genu_mask-mk' '2m-CC_Splenium_mask-FA' '2m-CC_Body_mask-eas_tort'
 'kut-CC_Splenium_mask-mk' 'kut-CC_Splenium_mask-ak' '2m-2_R_thal-ias_Da'
 'kut-2_R_thal-FA' 'kut-CC_Body_mask-ak' '4m-CC_Splenium_mask-ak'
 '3m-CC_Splenium_mask-mk' 'mean-2_R_thal-awf' '2m-2_R_thal-ak'
 '2m-2_R_thal-md' '2m-2_R_thal-awf' '3m-CC_Splenium_mask-rd'
 'mean-CC_Body_mask-awf' '2m-CC_Genu_mask-ak' '4m-2_R_thal-ias_Da'
 'kut-2_R_thal-ak' '3m-CC_Genu_mask-eas_De_perp' 'mean-2_R_thal-ias_Da'
 '4m-CC_Body_mask-FA' 'kut-CC_Genu_mask-ak' 'kut-2_R_thal-ias_Da'
 '3m-CC_Splenium_mask-md' 'std-1_L_thal-ias_Da'
 'kut-CC_Genu_mask-eas_De_par']


# Negative - Digit Span Backward T1

## Template Space - Old Mask

## Template Space - New Mask

* 1st iter:
	maximum test accuracy= 0.464, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
	Selected feature for 3xiter= [ 90. 129. 102.  83. 212. 192. 167. 205. 158. 143.]
	['eas_De_par-left_caudal-mean' 'eas_De_perp-left_caudal-etrp'
	 'eas_De_par-corpus_callosum-skew' 'eas_De_par-left_middle-kurt'
	 'md-left_rostral-skew' 'ias_Da-right_middle-skew' 'FA-right_caudal-skew'
	 'ias_Da-corpus_callosum-mean' 'FA-right_middle-kurt'
	 'FA-left_rostral-kurt']

* 2nd iter
	maximum test accuracy= 0.488, achieved by using 27 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
	Selected feature for 3xiter= [ 90. 129. 102.  83. 212. 192. 167. 205. 158. 143. 239.  97. 276. 134.
	  70.  29.  10.  31. 124. 181. 229. 186. 119. 139. 279.  69. 146.]
	['eas_De_par-left_caudal-mean' 'eas_De_perp-left_caudal-etrp'
	 'eas_De_par-corpus_callosum-skew' 'eas_De_par-left_middle-kurt'
	 'md-left_rostral-skew' 'ias_Da-right_middle-skew' 'FA-right_caudal-skew'
	 'ias_Da-corpus_callosum-mean' 'FA-right_middle-kurt'
	 'FA-left_rostral-kurt' 'md-right_caudal-etrp'
	 'eas_De_par-right_caudal-skew' 'mk-corpus_callosum-std'
	 'eas_De_perp-right_caudal-etrp' 'eas_De_par-left_rostral-mean'
	 'ak-right_caudal-etrp' 'ak-left_middle-mean' 'ak-corpus_callosum-std'
	 'eas_De_perp-right_middle-etrp' 'ias_Da-right_rostral-std'
	 'md-right_middle-etrp' 'ias_Da-left_middle-std'
	 'eas_De_perp-left_middle-etrp' 'eas_De_perp-corpus_callosum-etrp'
	 'mk-corpus_callosum-etrp' 'awf-corpus_callosum-etrp'
	 'FA-right_rostral-std']

## Subject Space - Old Mask

* 1st iter:
maximum test accuracy= 0.610, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
Selected feature for 3xiter= [ 88.  56.  98. 128.  27.  22.  47.  42. 103.  23.]
['FA-cc_genu-kurt' 'eas_De_par-thal-std' 'FA-thal-kurt' 'md-cc_genu-kurt'
 'awf-cc_genu-skew' 'awf-cc_body-skew' 'eas_De_par-cc_genu-skew'
 'eas_De_par-cc_body-skew' 'ias_Da-cc_body-kurt' 'awf-cc_body-kurt']

 * 2nd iter:
 maximum test accuracy= 0.645, achieved by using 22 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
Selected feature for 3xiter= [ 88.  56.  98. 128.  27.  22.  47.  42. 103.  23. 151.  33.   6.  15.
   1. 106.  11.  86.  16.  36.  85.  26.]
['FA-cc_genu-kurt' 'eas_De_par-thal-std' 'FA-thal-kurt' 'md-cc_genu-kurt'
 'awf-cc_genu-skew' 'awf-cc_body-skew' 'eas_De_par-cc_genu-skew'
 'eas_De_par-cc_body-skew' 'ias_Da-cc_body-kurt' 'awf-cc_body-kurt'
 'mk-cc_splenium-std' 'awf-cc_splenium-kurt' 'ak-cc_genu-std'
 'ak-thal-mean' 'ak-cc_body-std' 'ias_Da-cc_genu-std' 'ak-cc_splenium-std'
 'FA-cc_genu-std' 'ak-thal-std' 'awf-thal-std' 'FA-cc_genu-mean'
 'awf-cc_genu-std']

## Subject Space - New Mask

* 1st iter:
maximum test accuracy= 0.583, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.31623, 0.50000) from 14 metrics
Selected feature for 3xiter= [195. 102. 150. 155.  41. 149.  10.  49. 246. 186.]
['ias_Da-left_caudal-mean' 'eas_De_par-corpus_callosum-skew'
 'FA-left_middle-mean' 'FA-right_middle-mean' 'awf-right_rostral-std'
 'FA-right_rostral-etrp' 'ak-left_middle-mean' 'awf-left_middle-etrp'
 'mk-left_rostral-std' 'ias_Da-left_middle-std']

2nd iter:
maximum test accuracy= 0.678, achieved by using 16 features and ( C, Gamma, eps)= ( 1000.00000, 0.31623, 0.50000) from 14 metrics
Selected feature for 3xiter= [195. 102. 150. 155.  41. 149.  10.  49. 246. 186. 220.  80. 171. 161.
  31.  51.]
['ias_Da-left_caudal-mean' 'eas_De_par-corpus_callosum-skew'
 'FA-left_middle-mean' 'FA-right_middle-mean' 'awf-right_rostral-std'
 'FA-right_rostral-etrp' 'ak-left_middle-mean' 'awf-left_middle-etrp'
 'mk-left_rostral-std' 'ias_Da-left_middle-std' 'md-left_middle-mean'
 'eas_De_par-left_middle-mean' 'FA-corpus_callosum-std'
 'FA-left_caudal-std' 'ak-corpus_callosum-std' 'awf-right_middle-std']

## Subject Space - New Mask - NN

maximum test accuracy= 0.708, achieved by using 19 features and (Hu, Alpha, eps)= ( 10.00000, 0.01000, 0.00000) from 14 metrics
Selected feature for 3xiter= [195. 225. 102.  94. 119.  70. 196. 124.  68. 112.  30. 143. 141.  45.
  54.   1. 191. 171. 184.]
['ias_Da-left_caudal-mean' 'md-right_middle-mean'
 'eas_De_par-corpus_callosum-skew' 'eas_De_par-left_caudal-etrp'
 'eas_De_perp-left_middle-etrp' 'eas_De_par-left_rostral-mean'
 'ias_Da-left_caudal-std' 'eas_De_perp-right_middle-etrp'
 'awf-corpus_callosum-kurt' 'eas_De_perp-right_rostral-skew'
 'ak-corpus_callosum-mean' 'FA-left_rostral-kurt' 'FA-left_rostral-std'
 'awf-left_middle-mean' 'awf-right_middle-etrp' 'ak-left_rostral-std'
 'ias_Da-right_middle-std' 'FA-corpus_callosum-std'
 'ias_Da-right_rostral-etrp']




# Negative - Letter Number T1

## Subject Space - New Mask

* 1st iter:

maximum test accuracy= 0.497, achieved by using 10 features and ( C, Gamma, eps)= ( 10000.00000, 0.00178, 0.05000) from 14 metrics
Selected feature for 3xiter= [197. 172.  91. 248.  26.  76.   5.  53. 162. 196.]
['ias_Da-left_caudal-skew' 'FA-corpus_callosum-skew'
 'eas_De_par-left_caudal-std' 'mk-left_rostral-kurt' 'ak-right_caudal-std'
 'eas_De_par-right_rostral-std' 'ak-right_rostral-mean'
 'awf-right_middle-kurt' 'FA-left_caudal-skew' 'ias_Da-left_caudal-std']

* 2nd iter:

maximum test accuracy= 0.504, achieved by using 12 features and ( C, Gamma, eps)= ( 10000.00000, 0.00178, 0.05000) from 14 metrics
Selected feature for 3xiter= [197. 172.  91. 248.  26.  76.   5.  53. 162. 196.  61. 146.]
['ias_Da-left_caudal-skew' 'FA-corpus_callosum-skew'
 'eas_De_par-left_caudal-std' 'mk-left_rostral-kurt' 'ak-right_caudal-std'
 'eas_De_par-right_rostral-std' 'ak-right_rostral-mean'
 'awf-right_middle-kurt' 'FA-left_caudal-skew' 'ias_Da-left_caudal-std'
 'awf-right_caudal-std' 'FA-right_rostral-std']

## Subject Space - New Mask - NN

( 1000.0 , 0.01 ) value of (Hu, Alpha), and best feat indices= [196 162  26 246 262 201  35 206  79 157]
maximum test accuracy= 0.633, achieved by using 8 features and (Hu, Alpha, eps)= ( 100.00000, 0.01000, 0.00000) from 14 metrics
Selected feature for 3xiter= [ 32. 186. 137. 180. 156. 221. 205. 196.]
['ak-corpus_callosum-skew' 'ias_Da-left_middle-std'
 'eas_De_perp-corpus_callosum-skew' 'ias_Da-right_rostral-mean'
 'FA-right_middle-std' 'md-left_middle-std' 'ias_Da-corpus_callosum-mean'
 'ias_Da-left_caudal-std']


## Subject Space - Old Mask

1st iter:
maximum test accuracy= 0.221, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
Selected feature for 3xiter= [118.  88.  40.  76.  46. 115. 111.  85.  51.  42.]
['ias_Da-thal-kurt' 'FA-cc_genu-kurt' 'eas_De_par-cc_body-mean'
 'eas_De_perp-thal-std' 'eas_De_par-cc_genu-std' 'ias_Da-thal-mean'
 'ias_Da-cc_splenium-std' 'FA-cc_genu-mean' 'eas_De_par-cc_splenium-std'
 'eas_De_par-cc_body-skew']

2nd iter:

maximum test accuracy= 0.263, achieved by using 18 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.50000) from 14 metrics
Selected feature for 3xiter= [118.  88.  40.  76.  46. 115. 111.  85.  51.  42. 108.  22. 106. 101.
  41. 126.  66.  81.]
['ias_Da-thal-kurt' 'FA-cc_genu-kurt' 'eas_De_par-cc_body-mean'
 'eas_De_perp-thal-std' 'eas_De_par-cc_genu-std' 'ias_Da-thal-mean'
 'ias_Da-cc_splenium-std' 'FA-cc_genu-mean' 'eas_De_par-cc_splenium-std'
 'eas_De_par-cc_body-skew' 'ias_Da-cc_genu-kurt' 'awf-cc_body-skew'
 'ias_Da-cc_genu-std' 'ias_Da-cc_body-std' 'eas_De_par-cc_body-std'
 'md-cc_genu-std' 'eas_De_perp-cc_genu-std' 'FA-cc_body-std']
total time= 67.17274856567383

## Template Space - New Mask
1st iter:
maximum test accuracy= 0.492, achieved by using 10 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.50000) from 14 metrics
Selected feature for 3xiter= [258. 182. 121.  52. 246.  20.  40. 191. 141.  36.]
['mk-left_middle-kurt' 'ias_Da-right_rostral-skew'
 'eas_De_perp-right_middle-std' 'awf-right_middle-skew'
 'mk-left_rostral-std' 'ak-left_caudal-mean' 'awf-right_rostral-mean'
 'ias_Da-right_middle-std' 'FA-left_rostral-std' 'awf-left_rostral-std']
 
 2nd iter:
 maximum test accuracy= 0.527, achieved by using 42 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.50000) from 14 metrics
Selected feature for 3xiter= [258. 182. 121.  52. 246.  20.  40. 191. 141.  36. 176. 174. 209.  69.
 244. 104. 161. 151.  41. 279.  46. 171. 156. 251. 166.  51. 146.   4.
 150. 186. 170. 181.  31.  34.  56. 100.   5.  13.  86. 241.  25. 206.]
['mk-left_middle-kurt' 'ias_Da-right_rostral-skew'
 'eas_De_perp-right_middle-std' 'awf-right_middle-skew'
 'mk-left_rostral-std' 'ak-left_caudal-mean' 'awf-right_rostral-mean'
 'ias_Da-right_middle-std' 'FA-left_rostral-std' 'awf-left_rostral-std'
 'ias_Da-left_rostral-std' 'FA-corpus_callosum-etrp'
 'ias_Da-corpus_callosum-etrp' 'awf-corpus_callosum-etrp'
 'md-corpus_callosum-etrp' 'eas_De_par-corpus_callosum-etrp'
 'FA-left_caudal-std' 'FA-left_middle-std' 'awf-right_rostral-std'
 'mk-corpus_callosum-etrp' 'awf-left_middle-std' 'FA-corpus_callosum-std'
 'FA-right_middle-std' 'mk-right_rostral-std' 'FA-right_caudal-std'
 'awf-right_middle-std' 'FA-right_rostral-std' 'ak-left_rostral-etrp'
 'FA-left_middle-mean' 'ias_Da-left_middle-std' 'FA-corpus_callosum-mean'
 'ias_Da-right_rostral-std' 'ak-corpus_callosum-std'
 'ak-corpus_callosum-etrp' 'awf-left_caudal-std'
 'eas_De_par-corpus_callosum-mean' 'ak-right_rostral-mean'
 'ak-left_middle-kurt' 'eas_De_par-right_middle-std'
 'md-corpus_callosum-std' 'ak-right_caudal-mean'
 'ias_Da-corpus_callosum-std']

## Template Space - Old Mask
1st iter:
maximum test accuracy= 0.388, achieved by using 9 features and ( C, Gamma, eps)= ( 31.62278, 56.23413, 0.50000) from 14 metrics
Selected feature for 3xiter= [158.  68.  31. 199. 129. 140. 124.  66. 189.]
['FA-CC_Genu_mask-kurt' 'awf-R_Pref-kurt' 'ak-R_Pref-std'
 'ias_Da-CC_Splenium_mask-etrp' 'eas_De_perp-CC_Splenium_mask-etrp'
 'FA-1_L_thal-mean' 'eas_De_perp-CC_Genu_mask-etrp' 'awf-R_Pref-std'
 'ias_Da-CC_Body_mask-etrp']
total time= 707.6866717338562


# All - Digit Span Backward T1

## Subject Space - New Mask
1st iter: maximum test accuracy= 0.394, achieved by using 10 features and ( C, Gamma, eps)= ( 1.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [ 32.  98. 197.  95. 163.  94. 137.  12. 248. 208.]
['ak-corpus_callosum-skew' 'eas_De_par-right_caudal-kurt'
 'ias_Da-left_caudal-skew' 'eas_De_par-right_caudal-mean'
 'FA-left_caudal-kurt' 'eas_De_par-left_caudal-etrp'
 'eas_De_perp-corpus_callosum-skew' 'ak-left_middle-skew'
 'mk-left_rostral-kurt' 'ias_Da-corpus_callosum-kurt']

2nd iter:
maximum test accuracy= 0.418, achieved by using 37 features and ( C, Gamma, eps)= ( 1.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [ 32.  98. 197.  95. 163.  94. 137.  12. 248. 208.  17. 195. 177. 224.
 147.  96. 271. 152. 205.  55. 165. 200. 157.  11.  61.  10. 160.  16.
  26. 166.  45.  60. 146.  56. 176. 171. 161.]
['ak-corpus_callosum-skew' 'eas_De_par-right_caudal-kurt'
 'ias_Da-left_caudal-skew' 'eas_De_par-right_caudal-mean'
 'FA-left_caudal-kurt' 'eas_De_par-left_caudal-etrp'
 'eas_De_perp-corpus_callosum-skew' 'ak-left_middle-skew'
 'mk-left_rostral-kurt' 'ias_Da-corpus_callosum-kurt'
 'ak-right_middle-skew' 'ias_Da-left_caudal-mean'
 'ias_Da-left_rostral-skew' 'md-left_middle-etrp' 'FA-right_rostral-skew'
 'eas_De_par-right_caudal-std' 'mk-right_caudal-std' 'FA-left_middle-skew'
 'ias_Da-corpus_callosum-mean' 'awf-left_caudal-mean'
 'FA-right_caudal-mean' 'ias_Da-right_caudal-mean' 'FA-right_middle-skew'
 'ak-left_middle-std' 'awf-right_caudal-std' 'ak-left_middle-mean'
 'FA-left_caudal-mean' 'ak-right_middle-std' 'ak-right_caudal-std'
 'FA-right_caudal-std' 'awf-left_middle-mean' 'awf-right_caudal-mean'
 'FA-right_rostral-std' 'awf-left_caudal-std' 'ias_Da-left_rostral-std'
 'FA-corpus_callosum-std' 'FA-left_caudal-std']

## Subject Space - Old Mask
1st iter:

maximum test accuracy= 0.377, achieved by using 10 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [154. 163. 137. 271. 258. 262. 236.   2. 131. 169.]
['FA-left_middle-etrp' 'FA-left_caudal-kurt'
 'eas_De_perp-corpus_callosum-skew' 'mk-right_caudal-std'
 'mk-left_middle-kurt' 'mk-right_middle-skew' 'md-right_caudal-std'
 'ak-left_rostral-skew' 'eas_De_perp-right_caudal-std'
 'FA-right_caudal-etrp']

## Template Space - New Mask

maximum test accuracy= 0.394, achieved by using 10 features and ( C, Gamma, eps)= ( 1.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [ 32.  98. 197.  95. 163.  94. 137.  12. 248. 208.]
['ak-corpus_callosum-skew' 'eas_De_par-right_caudal-kurt'
 'ias_Da-left_caudal-skew' 'eas_De_par-right_caudal-mean'
 'FA-left_caudal-kurt' 'eas_De_par-left_caudal-etrp'
 'eas_De_perp-corpus_callosum-skew' 'ak-left_middle-skew'
 'mk-left_rostral-kurt' 'ias_Da-corpus_callosum-kurt']
total time= 2452.376142978668

## Template Space - Old Mask


# All - Letter Number T1

## Template Space - New Mask

1st iter:
maximum test accuracy= 0.335, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [ 30. 246. 168.  20. 160. 261. 145. 201.  21. 196.]
['ak-corpus_callosum-mean' 'mk-left_rostral-std' 'FA-right_caudal-kurt'
 'ak-left_caudal-mean' 'FA-left_caudal-mean' 'mk-right_middle-std'
 'FA-right_rostral-mean' 'ias_Da-right_caudal-std' 'ak-left_caudal-std'
 'ias_Da-left_caudal-std']

2nd iter
maximum test accuracy= 0.348, achieved by using 12 features and ( C, Gamma, eps)= ( 500.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [ 30. 246. 168.  20. 160.  86.   7. 186.  56.  76. 156.  26.]
['ak-corpus_callosum-mean' 'mk-left_rostral-std' 'FA-right_caudal-kurt'
 'ak-left_caudal-mean' 'FA-left_caudal-mean' 'eas_De_par-right_middle-std'
 'ak-right_rostral-skew' 'ias_Da-left_middle-std' 'awf-left_caudal-std'
 'eas_De_par-right_rostral-std' 'FA-right_middle-std'
 'ak-right_caudal-std']

## Subject Space - New Mask

maximum test accuracy= 0.475, achieved by using 24 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [163.  32.  62. 158.  78. 160. 196.  31. 176. 166.  11.  56.  16.  36.
  35. 161. 141.  41. 146. 171.  86. 206.   1.  61.]
['FA-left_caudal-kurt' 'ak-corpus_callosum-skew' 'awf-right_caudal-skew'
 'FA-right_middle-kurt' 'eas_De_par-right_rostral-kurt'
 'FA-left_caudal-mean' 'ias_Da-left_caudal-std' 'ak-corpus_callosum-std'
 'ias_Da-left_rostral-std' 'FA-right_caudal-std' 'ak-left_middle-std'
 'awf-left_caudal-std' 'ak-right_middle-std' 'awf-left_rostral-std'
 'awf-left_rostral-mean' 'FA-left_caudal-std' 'FA-left_rostral-std'
 'awf-right_rostral-std' 'FA-right_rostral-std' 'FA-corpus_callosum-std'
 'eas_De_par-right_middle-std' 'ias_Da-corpus_callosum-std'
 'ak-left_rostral-std' 'awf-right_caudal-std']

## Template Space - Old Mask

maximum test accuracy= 0.223, achieved by using 10 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [195. 163. 272. 157. 180. 167.  82. 186. 190. 185.]
['ias_Da-CC_Splenium_mask-mean' 'FA-CC_Splenium_mask-kurt'
 'mk-L_Pref-skew' 'FA-CC_Genu_mask-skew' 'ias_Da-2_R_thal-mean'
 'FA-L_Pref-skew' 'eas_De_par-CC_Body_mask-skew' 'ias_Da-CC_Body_mask-std'
 'ias_Da-CC_Genu_mask-mean' 'ias_Da-CC_Body_mask-mean']

## Subject Space - Old Mask
maximum test accuracy= 0.368, achieved by using 10 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [105.  78.   9. 150.  11.   0.  52. 110. 145.  91.]
['ias_Da-cc_genu-mean' 'eas_De_perp-thal-kurt' 'ak-cc_genu-etrp'
 'mk-cc_splenium-mean' 'ak-cc_splenium-std' 'ak-cc_body-mean'
 'eas_De_par-cc_splenium-skew' 'ias_Da-cc_splenium-mean' 'mk-cc_genu-mean'
 'FA-cc_splenium-std']


 Some Courious result using random forest

 ( 500 , 0.31623 ) value of (C, Gamma), and best feat indices= [245]
maximum test accuracy= 0.454, achieved by using 1 features and ( C, Gamma, eps)= ( 500.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [245.]
['mk-left_rostral-mean']
total time= 116.95876502990723

maximum test accuracy= 0.493, achieved by using 6 features and ( C, Gamma, eps)= ( 500.00000, 0.31623, 0.05000) from 14 metrics
Selected feature for 3xiter= [236. 198.  32. 132.  26. 133.]
['md-right_caudal-std' 'ias_Da-left_caudal-kurt' 'ak-corpus_callosum-skew'
 'eas_De_perp-right_caudal-skew' 'ak-right_caudal-std'
 'eas_De_perp-right_caudal-kurt']
