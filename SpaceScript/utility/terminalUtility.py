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

def termThreadEventHandler(holdValue_v, pullString_q, commandPipe, ParentHoldValue_v):
	if holdValue_v.value == True:
		commandString_str = safePull(pullString_q)
		parsedCommandString_arr = commandString_str.split(" ")
		#would like to add command dictionary to double check command
		command_str = parsedCommandString_str[0] 
		parsedCommandString_arr.remove(command_str)
		arguments_arr = parsedCommandString_str
		commandPipe.send([command_str, arguments_arr])
		ParentHoldValue_v.value = 1
		backgroundEventHandler_bool = True
		return True
	else:
		return False