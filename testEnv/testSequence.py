import sys
settings = open("settings.txt", "r")
path_str = settings.readline().replace("path = ", "")
#enter additional settings here
settings.close()

pythonCompatiblePath_str = path_str.replace(chr(92), "/")

sys.path.append(pythonCompatiblePath_str)

#needed to adapt sys.path so main import is coming now
import testEnv
from testEnv import frontEnd
from testEnv import utility
from testEnv.utility import vectorAlgebraFunctional

runthroughs_arr = []

def runthroughAppend(returned_arr):
	for index in range(len(returned_arr)):
		runthroughs.append(returned_arr[index])
	else:
		return True

def failureCheck():
	for index in range(len(runthroughs)):
		if runthroughs[index] == False:
			return 
		else:
			pass
	else:
		return True

def failureSearch(index_int):
	for iteration in range(len(functionRunthroughs_arr)):
		index_int -= functionRunthroughs_arr[iteration]
		if index_int < 0:
			index_int += functionRunthroughs_arr[iteration]
			failure_arr = [functionNames_arr[iteration], index_int]
			return failure_arr
		else:
			pass
	else:
		return None

def main():
	for index in range(len(function_arr)):
		runthroughAppend(function_arr[index]())
	else:
		check = failureCheck()
		if check:
			print("Testing Done! Everything seems to work!")
			return True
		else:
			failure_arr = failureSearch(check)
			print("An Error occured in function " + failure_arr[0] + 
				  "! \n At runthrough " + failure_arr[1] + ";")


function_arr = [testEnv.utility.vectorAlgebraFunctional.dimensionCheckFatal,
				 testEnv.utility.vectorAlgebraFunctional.dimensionCheck,
				 testEnv.utility.vectorAlgebraFunctional.add,
				 testEnv.utility.vectorAlgebraFunctional.dotProduct,
				 testEnv.utility.vectorAlgebraFunctional.vectorScalarProduct,
				 testEnv.utility.vectorAlgebraFunctional.length,
				 testEnv.utility.vectorAlgebraFunctional.crossProduct,
				 testEnv.utility.vectorAlgebraFunctional.invert,
				 testEnv.utility.vectorAlgebraFunctional.angle]

functionRunthroughs_arr = [2, 2, 2, 2, 2, 2, 1, 2, 2]
functionNames_arr = ["utility/vectorAlgebra/dimensionCheckFatal",
					  "utility/vectorAlgebra/dimensionCheck",
					  "utility/vectorAlgebra/add",
					  "utility/vectorAlgebra/dotProduct",
					  "utility/vectorAlgebra/vectorScalarProduct",
					  "utility/vectorAlgebra/length",
					  "utility/vectorAlgebra/crossProduct",
					  "utility/vectorAlgebra/invert",
					  "utility/vectorAlgebra/angle"]

#main segment
main()