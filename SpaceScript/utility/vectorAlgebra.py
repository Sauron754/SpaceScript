import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import utility

def dimensionCheckFatal(A, B):
	if len(A) != len(B):
		raise SpaceScript.exceptions.utility.dimensionError("vector dimensions 												   not equal")

def dimensionCheck(A, B):
	equalDimensions = False
	if len(A) == len(B):
		equalDimensions = True
	else:
		equalDimensions = False
	return equalDimensions
	
def add(A, B):
	dimensionCheckFatal(A, B)
	vectorOut = []
	for iteration in range(len(A)):
		vectorOut.append(A[iteration] + B[iteration])
	return vectorOut

def scalarProduct(A, B):
	dimensionCheckFatal(A, B)
	scalar = 0
	for iteration in range(len(A)):
		scalar += A[iteration] * B[iteration]
	return scalar