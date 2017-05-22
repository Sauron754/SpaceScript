def argumentCountCheck(argumentNumber, *args):
	if argumentNumber !== len(args):
		raise argumentCountError("Invalid Argument Count", "Please retry!")
		return False
	else:
		return True