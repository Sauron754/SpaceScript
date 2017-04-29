import SpaceScript
from SpaceScript import data
from SpaceScript.data import dataHandler

def help(*args):
	#when finished will return help for desired command

def new(*args):
	if args[0] == "save":
		SpaceScript.data.dataHandler.newWorldSave(args[1])
	#append list of all 'new' options

def load(*args):
	if args[0] == "world":
		#now we need to add a save reading mechanism here or maybe we might open
		#a new .py file in the data package which will then handle the saving
		#writing routines, then we only need to call this module when we want
		#to perform a sandardized load/save