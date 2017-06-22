import SpaceScript
from SpaceScript import data
from SpaceScript import utility
from SpaceScript.data import dataHandler
from SpaceScript.utility import terminalUtility
from SpaceScript.utility.terminalUtility import terminalOutput as terminalOutput


maxArguments_dict = {"help": 1, "new": , "load":, }

def help(*args):
	try:
		SpaceScript.utility.terminalUtility.argumentCountCheck(
												maxArguments_dict["help"], args)
	except argumentCountError:
		terminalOutput("Invalid number of Arguments")
	#when finished will return help for desired command

def new(*args):
	try:
		SpaceScript.utility.terminalUtility.argumentCountCheck(
												maxArguments_dict["new"], args)
	except argumentCountError:
		terminalOutput("Invalid number of Arguments")
	if args[0] == "save":
		SpaceScript.data.dataHandler.newWorldSave(args[1])
	#append list of all 'new' options

def load(*args):
	try:
		SpaceScript.utility.terminalUtility.argumentCountCheck(
												maxArguments_dict["load"], args)
	except argumentCountError:
		terminalOutput("Invalid number of Arguments")
	if args[0] == "world":
		#now we need to add a save reading mechanism here or maybe we might open
		#a new .py file in the data package which will then handle the saving
		#writing routines, then we only need to call this module when we want
		#to perform a sandardized load/save
	elif args[0] == "craft":
		#loadCraft
	elif args[0] == "flight":
		#loadFlight
	