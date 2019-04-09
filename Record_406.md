# Negative - T1 Letter Number

* from 10 valid feature to 20 valid features, 11 of them are new statistics
* 1st iter grid search hyperparameter using less than 10 feature, 2nd iter expand to all valid feature number

* 1st iter: 
	* maximum test accuracy= 0.400, achieved by using 10 features and ( C, Gamma, eps)= ( 1000.000, 0.002, 0.050) from 14 metrics
	* Selected feature for 3xiter= [228.  53. 239. 305.  10. 111. 197. 109. 275. 149.]
	* ['3m-CC_Splenium_mask-ad' 'mean-CC_Splenium_mask-eas_tort'
	 '3m-CC_Splenium_mask-rk' 'kut-1_L_thal-eas_tort' 'mean-1_L_thal-rd'
	 'std-CC_Splenium_mask-eas_De_par' '3m-2_R_thal-eas_tort'
	 'std-CC_Splenium_mask-ak' '4m-CC_Body_mask-rk' '2m-CC_Body_mask-eas_tort']

* 2nd iter:
	* maximum test accuracy= 0.502, achieved by using 20 features and ( C, Gamma, eps)= ( 1000.000, 0.002, 0.050) from 14 metrics
	* Selected feature for 3xiter= [228.  53. 239. 305.  10. 111. 197.  19. 275. 149.  77.  47. 234. 235. 351. 112. 337. 109. 320. 236.]
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
	* Selected feature for 3xiter= [341. 149. 358. 102. 269.  53. 335. 203.  41. 319.]
	['kut-CC_Genu_mask-eas_tort' '2m-CC_Body_mask-eas_tort'
	 'kut-CC_Splenium_mask-rd' 'std-CC_Genu_mask-FA'
	 '4m-CC_Body_mask-eas_tort' 'mean-CC_Splenium_mask-eas_tort'
	 'kut-CC_Body_mask-rk' '3m-2_R_thal-rk' 'mean-CC_Genu_mask-eas_tort'
	 'kut-2_R_thal-ias_Da']

* 2nd iter:
	* maximum test accuracy= 0.404, achieved by using 58 features and ( C, Gamma, eps)= ( 1000.00000, 0.00178, 0.10000) from 14 metrics
	* Selected feature for 3xiter= [341. 149. 358. 102. 269.  53. 335. 203.  41. 319.  13. 118. 114.  14.
	355. 283. 337.  61. 277. 223. 212. 271. 357.  25. 214. 116. 254. 104.
	211.  42. 350. 343. 115. 331. 157. 213. 328.  67. 158. 187. 152. 284.
	332. 153. 154. 278. 279. 195.  87.  63.  70. 189. 183.  69.  64. 190.
	184.  45.]
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
	* Selected feature for 3xiter= [216. 107. 165. 358. 149.  71. 359.  41.  53. 319.  29. 222. 275. 173.
	 102. 210. 138.  55. 180. 331. 237.  32. 339.  66. 332.  56. 182. 225.
	 193.  81. 183.  68. 190.  70.  64. 184. 189.  63.  76.  88. 273. 274.
	  69.  87.  75. 279.  51. 153. 340.  39. 196. 201.  74. 280. 194.  34.
	 334.  82. 286.]
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
Selected feature for 3xiter= [210. 209. 104. 105. 174. 149. 357. 349. 139. 318.]
['3m-CC_Body_mask-FA' '3m-CC_Body_mask-eas_tort' 'std-CC_Genu_mask-md'
 'std-CC_Genu_mask-mk' '2m-CC_Splenium_mask-FA' '2m-CC_Body_mask-eas_tort'
 'kut-CC_Splenium_mask-mk' 'kut-CC_Splenium_mask-ak' '2m-2_R_thal-ias_Da'
 'kut-2_R_thal-FA']

 maximum test accuracy= 0.368, achieved by using 30 features and ( C, Gamma, eps)= ( 31.62278, 0.31623, 0.50000) from 14 metrics
Selected feature for 3xiter= [210. 209. 104. 105. 174. 149. 357. 349. 139. 318. 325. 289. 237.  14.
 133. 140. 134. 238.  26. 157. 259. 313. 220.  19. 270. 337. 319. 236.
  67. 339.]
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