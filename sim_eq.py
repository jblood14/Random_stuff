#Code written by James W. Blood, June 2017
import numpy as np #import numpy for matrix manipulation
def solve_eqs(values):
	'''take in list of lists or np arrays and return array of
	values for unknown variables.'''
	#check if the elements of values are np arrays 
	checked=[]
	for v in values:
		if type(v) == list:
			checked.append(np.asarray(v)) #if not, make them arrays and append to checked
		else:
			checked.append(v) #if they are, then append as is
	#make coeffecient and results arrays
	coeffs=np.stack([eq[:-1] for eq in checked])
	results=np.stack([eq[-1]for eq in checked])
	#solve eqns and return variables
	return np.dot(np.linalg.inv(coeffs),results)