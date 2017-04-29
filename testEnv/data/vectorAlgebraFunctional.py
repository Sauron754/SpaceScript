#Functional Test of vectorAlgebra module
#
#
import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import vectorAlgebra

def dimensionCheckFatal():
	argumentsValid = [[1, 2], [2, 1]]
	argumentsInvalid = [[1, 2], [1, 2, 3]]
	runthroughs = []
	try:
		SpaceScript.utility.vectorAlgebra.dimensionCheckFatal(argumentsValid[0]
															  argumentsValid[1])
		runthroughs.append(True)
	except:
		runthroughs.append(False)
	try:
		SpaceScript.utility.vectorAlgebra.dimensionCheckFatal(
			argumentsInvalid[0], argumentsInvalid[1])
		runthroughs.append(False)
	except dimensionError: