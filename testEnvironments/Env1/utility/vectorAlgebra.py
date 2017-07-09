import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import utility
import math

def dimensionCheckFatal(A_arr, B_arr):
	if len(A_arr) != len(B_arr):
		raise SpaceScript.exceptions.utility.dimensionError(
			"vector dimensions not equal")

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

def dotProduct(A_arr, B_arr):
	dimensionCheckFatal(A_arr, B_arr)
	scalar_float = 0
	for iteration in range(len(A_arr)):
		scalar_float += A_arr[iteration] * B_arr[iteration]
	return scalar_float

def vectorScalarProduct(A_arr, scalar_float):
	vectorOut_arr = []
	for iteration in range(len(A_arr)):
		vectorOut_arr.append(A_arr[iteration] * scalar_float)
	return vectorOut_arr

def length(A_arr):
	dimensionSum_float = 0
	for iteration in range(len(A_arr)):
		dimensionSum_float += (A_arr[iteration]**2)
	length_float = math.sqrt(dimensionSum_float)
	return length_float

def crossProduct(A_arr, B_arr):
	if len(A_arr) != 3:
		raise SpaceScript.exceptions.utility.dimensionError(
			"A_arr is not 3 dimensional")
	if len(B_arr) != 3:
		raise SpaceScript.exceptions.utility.dimensionError(
			"B_arr is not 3 dimensional")
	vectorOut_arr = []
	vectorOut_arr.append(A_arr[1] * B_arr[2] - A_arr[2] * B_arr[1])
	vectorOut_arr.append(A_arr[2] * B_arr[0] - A_arr[0] * B_arr[2])
	vectorOut_arr.append(A_arr[0] * B_arr[1] - A_arr[1] * B_arr[0])
	return vectorOut_arr

def invert(A_arr):
	vectorOut_arr = []
	for iteration in range(len(A_arr)):
		vectorOut_arr.append(-1 * A_arr[iteration])
	return vectorOut_arr

def angle(A_arr, B_arr):
	dimensionCheckFatal(A_arr, B_arr)
	angle = math.acos(dotProduct(A_arr, B_arr) / (length(A_arr) * length(B_arr)))
	return angle

def unitVector(A_arr):
	factor = 1 / length(A_arr)
	vectorOut_arr = vectorScalarProduct(A_arr, factor)
	return vectorOut_arr