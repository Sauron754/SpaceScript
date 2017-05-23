import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import frontEnd
from SpaceScript.exceptions.frontEnd import argumentCountError as argumentCountError

def argumentCountCheck(argumentNumber_int, *args):
	if argumentNumber_int !== len(args):
		raise argumentCountError("Invalid Argument Count", "Please retry!")
		return False
	else:
		return True