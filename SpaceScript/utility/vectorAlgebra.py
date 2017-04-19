def add(A, B):
	if len(A) != len(B):
		raise SpaceScript.exceptions.utility.dimensionError(
			"Line 3 in <module> myArray", "vector dimensions not equal")
	vectorOut = []
	for iteration in range(len(A)):
		vectorOut.appen(A[iteration] + B[iteration])
	return vectorOut

def scalarProduct(A, B):
	scalar = 0
	for iteration in range(len(A)):
		scalar += A[iteration] * B[iteration]
	return scalar