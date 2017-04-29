#Functional Test of vectorAlgebra module
#
#
import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import vectorAlgebra

def dimensionCheckFatal():
	argumentsValid_arr = [[1, 2], [2, 1]]
	argumentsInvalid_arr = [[1, 2], [1, 2, 3]]
	runthroughs_arr = []
	try:
		SpaceScript.utility.vectorAlgebra.dimensionCheckFatal(
			argumentsValid_arr[0], argumentsValid_arr[1])
		runthroughs_arr.append(True)
	except:
		runthroughs_arr.append(False)
	try:
		SpaceScript.utility.vectorAlgebra.dimensionCheckFatal(
			argumentsInvalid_arr[0], argumentsInvalid_arr[1])
		runthroughs_arr.append(False)
	except dimensionError:
		runthroughs_arr.append(True)
	except:
		runthroughs_arr.append(False)
	for element in runthroughs_arr:
		if element != True:
			return False
	else:
		return True

def dimensionCheck():
	argumentsValid_arr = [[1, 2], [2, 1]]
	argumentsInvalid_arr = [[1, 2], [1, 2, 3]]
	runthroughs_arr = []
	if SpaceScript.utility.vectorAlgebra.dimensionCheck(argumentsValid_arr) == True:
		runthroughs_arr.append(True)
	else:
		runthroughs_arr.append(False)
	if SpaceScript.utility.vectorAlgebra.dimensionCheck(argumentsInvalid_arr) == False:
		runthroughs_arr.append(True)
	else:
		runthroughs_arr.append(False)
	for element in runthroughs_arr:
		if element != True:
			return False
	else:
		return True

def add():
	arguments1_arr = [[1, 3], [4, 3]]
	arguments2_arr = [[1, 2, 3], [4, 5, 6]]
	results1_arr = [5, 6]
	results2_arr = [5, 7, 9]
	runthroughs_arr = []
	testResults1_arr = SpaceScript.utility.vectorAlgebra.add(
		arguments1_arr[0], arguments1_arr[1])
	testResults2_arr = SpaceScript.utility.vectorAlgebra.add(
		arguments2_arr[0], arguments2_arr[1])
	if testResults1_arr == results1_arr:
		runthroughs_arr.append(True)
	else:
		runthroughs_arr.append(False)
	if testResults2_arr == results2_arr:
		runthroughs_arr.append(True)
	else:
		runthroughs_arr.append(False)
	for element in runthroughs_arr:
		if element != True:
			return False
	else:
		return True