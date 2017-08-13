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
from testEnv.frontEnd import terminal
from testEnv.utility import vectorAlgebraFunctional

functions_dict = {"frontEnd/terminal/clientTerminalIOTest":
				  testEnv.frontEnd.terminal.clientTerminalIOTest, 
				  "utility/vectorAlgebra/dimensionCheckFatal":
				  testEnv.utility.vectorAlgebraFunctional.dimensionCheckFatal,
				  "utility/vecotrAlgebra/dimensionCheck":
				  testEnv.utility.vectorAlgebraFunctional.dimensionCheck,
				  "utility/vectorAlgebra/add":
				  testEnv.utility.vectorAlgebraFunctional.add,
				  "utility/vectorAlgebra/dotProduct":
				  testEnv.utility.vectorAlgebraFunctional.dotProduct,
				  "utility/vectorAlgebra/vectorScalarProduct":
				  testEnv.utility.vectorAlgebraFunctional.vectorScalarProduct,
				  "utility/vectorAlgebra/length":
				  testEnv.utility.vectorAlgebraFunctional.length,
				  "utility/vectorAlgebra/crossProduct":
				  testEnv.utility.vectorAlgebraFunctional.crossProduct,
				  "utility/vectorAlgebra/invert":
				  testEnv.utility.vectorAlgebraFunctional.invert,
				  "utility/vectorAlgebra/angle":
				  testEnv.utility.vectorAlgebraFunctional.angle}

noneReturnFunctions_arr = ["frontEnd/terminal/clientTerminalIOTest"]

def elementOf(element, list_arr):
	for iteration in range(len(list_arr)):
		if element == list_arr[iteration]:
			return True
		else:
			pass
	else:
		return False

def main():
	continue_str = "y"
	while continue_str == "y":
		continue_str = str(input("Continue: "))
		command_str = str(input("Function: "))
		runthrough = functions_dict[command_str]()
		if command_str != elementOf(command_str, noneReturnFunctions_arr):
			try:
				index = runthrough.index(False)
				print("Error at runthrough" + str(index + 1))
			except ValueError:
				print("Function is working clean!")
		else:
			print("Function has finished working")
	else:
		return True

#main run loop
main()