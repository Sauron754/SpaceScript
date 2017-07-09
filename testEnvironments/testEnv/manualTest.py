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
				  testEnv.utility.vectorAlgebra.dimensionCheckFatal,
				  "utility/vecotrAlgebra/dimensionCheck":
				  testEnv.utility.vectorAlgebra.dimensionCheck,
				  "utility/vectorAlgebra/add":
				  testEnv.utility.vectorAlgebra.add,
				  "utility/vectorAlgebra/dotProduct":
				  testEnv.utility.vectorAlgebra.dotProduct,
				  "utility/vectorAlgebra/vectorScalarProduct":
				  testEnv.utility.vectorAlgebra.vectorScalarProduct,
				  "utility/vectorAlgebra/length":
				  testEnv.utility.vectorAlgebra.length,
				  "utility/vectorAlgebra/crossProduct":
				  testEnv.utility.vectorAlgebra.crossProduct,
				  "utility/vectorAlgebra/invert":
				  testEnv.utility.vectorAlgebra.invert,
				  "utility/vectorAlgebra/angle":
				  testEnv.utility.vectorAlgebra.angle}

def main():
	continue_str = "y"
	while continue_str == "y":
		continue_str = str(input("Continue: "))
		command_str = str(input("Function: "))
		runthrough = functions_dict[command_str]()
		try:
			index = runthrough.index(False)
			print("Error at runthrough" + str(index + 1))
		except ValueError:
			print("Function is working clean!")
	else:
		return True

#main run loop
main()