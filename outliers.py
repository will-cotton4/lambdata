'''
This function detects (and, optionally, removes) outliers 
given a maximum number of standard deviations allowed 
from the mean for a list.
'''

def outliers(data_orig, threshold=1.5, remove=False):
	data = data_orig
	mean = np.mean(data)
	std = np.std(data)
	outlier_list = []
	# Check z-score (number of std. deviations from mean)
	# for each item in data.
	for item in data:
		z = np.abs(item-mean)/std
		if z > threshold:
			outlier_list.append(item)
	# If the remove parameter is true, remove outliers and return
	# the edited list.
	if remove == True:
		for outlier in outlier_list:
			data.remove(outlier)
		print('Outliers removed!')
	# If the remove parameter is false, just count and display the outliers.
	else:
		outlier_count = len(outlier_list)
		print(outlier_count, 'Outliers detected:')
		print(outlier_list)
	return data

