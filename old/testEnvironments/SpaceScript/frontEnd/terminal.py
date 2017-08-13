from appJar import gui
from multiprocessing import Queue

def clientTerminal(pullString_q, pushString_q, holdValue_v, parentHoldValue_v):
	global term
	global transferPullQueue_q
	global transferPushQueue_q
	global transferParentHold_v
	global transferHold_v
	transferParentHold_v = parentHoldValue_v
	transferHold_v = holdValue_v
	transferPullQueue_q = pullString_q
	transferPushQueue_q = pushString_q
	term = gui()
	term.addListBox("mainOutput", ["Big thank you to appJar", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "For more information type license"])
	term.addEntry("commandLine")
	term.enableEnter(submit)
	term.registerEvent(terminalRefresh)
	term.setPollTime(1)
	app.go()

def submit(key):
	inputString_str = term.getEntry("commandLine")
	transferPullQueue_q.put(inputString_str)
	transferParentHold_v.value = True
	term.addListItems("commandLine", [inputString_str])
	return True

def terminalRefresh():
	if transferHold_v.value:
		term.addListItems("commandLine", [safePull(transferPushQueue_q)])
		return True
	else:
		return False

def terminal(option, pullString_q, pushString_q, holdValue_v, parentHoldValue_v):
	if option == 0:
		clientTerminal(pullString_q, pushString_q, holdValue_v, parentHoldValue_v)
		return True
	else:
		return False