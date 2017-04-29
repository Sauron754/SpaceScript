import SpaceScript
from SpaceScript import frontEnd
from SpaceScript.frontEnd import bashFunctions

def midParser(command_str):
	commandSplit_str = command_str.split(" ")
	arguments = []
	for element in commandSplit_str:
		if element != commandSplit_str[0]:
			arguments.append(element)
	eval('SpaceScript.frontEnd.bashFunctions.' + commandSplit_str[0])(arguments)