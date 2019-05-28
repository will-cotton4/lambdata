import pandas as pd
'''
This function checks each column of a dataframe and
prints the ones that are missing values along with
a count of those missing values.
'''
def check_nulls(df):
	# Create a copy for safety
	df = df.copy()

	# For each column in the dataframe, if missing values,
	# print number missing
	for column in df.columns:
		null_count = df[column].isnull().sum()
		if null_count != 0:
			print(column, 'is missing', null_count, 'values.')
	return
