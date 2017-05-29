import multiprocessing
import queue
import SpaceScript
from SpaceScript import exceptions
from SpaceScript.exceptions import frontEnd
from SpaceScript.exceptions.frontEnd import argumentCountError as argumentCountError

def argumentCountCheck(argumentNumber_int, arguments_arr):
	if argumentNumber_int !== len(arguments_arr):
		raise argumentCountError("Invalid Argument Count", "Please retry!")
		return False
	else:
		return True

def safePull(queue):
	try:
		querry = queue.get_nowait()
		return querry
	except queue.Empty:
		return chr(0)
