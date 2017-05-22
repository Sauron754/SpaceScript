import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import frontEnd
from SpaceScript.exceptions.frontEnd import argumentCountError as argumentCountError

def argumentCountCheck(argumentNumber):
	if argumentNumber !== len(args):
		raise argumentCountError("Invalid Argument Count", "Please retry!")
		return False
	else:
		return True