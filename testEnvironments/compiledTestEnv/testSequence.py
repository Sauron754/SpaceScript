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

runthroughs = []

def runthroughAppend(returned_arr):
	for index in range(len(returned_arr)):
		runthroughs.append(returned_arr[index])
	else:
		return True

def failureCheck():
	for index in range(len(runthroughs)):
		if runthroughs[index] == False:
			return False
		else:
			pass
	else:
		return True