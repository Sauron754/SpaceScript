import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import utility

def dimensionCheckFatal(A_arr, B_arr):
	if len(A_arr) != len(B_arr):
		raise SpaceScript.exceptions.utility.dimensionError("vector dimensions 												   not equal")

def dimensionCheck(A_arr, B_arr):
	equalDimensions_bool = False
	if len(A_arr) == len(B_arr):
		equalDimensions_bool = True
	else:
		equalDimensions_bool = False
	return equalDimensions_bool

def add(A_arr, B_arr):
	dimensionCheckFatal(A_arr, B_arr)
	vectorOut_arr = []
	for iteration in range(len(A_arr)):
		vectorOut_arr.append(A_arr[iteration] + B_arr[iteration])
	return vectorOut_arr

def scalarProduct(A_arr, B_arr):
	dimensionCheckFatal(A_arr, B_arr)
	scalar_float = 0
	for iteration in range(len(A_arr)):
		scalar_float += A_arr[iteration] * B_arr[iteration]
	return scalar_float

def length(A_arr):
	dimensionSum_float = 0
	for iteration in range(len(A_arr)):
		dimensionSum_float += (A_arr[iteration]**2)
	length_float = sqrt(dimensionSum_float)
	return length_float


