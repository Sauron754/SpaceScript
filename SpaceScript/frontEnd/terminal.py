from appJar import gui
from multiprocessing import Queue

def clientTerminal(pullString_q, pushString_q, holdValue_v, ParentHoldValue_v):
	global term
	global transferPullQueue_q
	global transferPushQueue_q
	global transferParentHold_v
	global transferHold_v
	transferParentHold_v = ParentHoldValue_v
	transferHold_v = holdValue_v
	transferPullQueue_q = pullString_q
	transferPushQueue_q = pushString_q
	term = gui()
	term.addListBox("mainOutput", ["Big thank you to appJar", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "For more information type license"])
	term.addEntry("BASH")
	term.enableEnter(submit)
	term.registerEvent(terminalRefresh)
	term.setPollTime(1)
	app.go()

def submit(key):
	inputString_str = term.getEntry("BASH")
	transferQueue_q.put(inputString_str)
	transferParentHold_v.value = True
	return True

def terminalRefresh():
	if transferHold_v.value:
		term.addListItems("BASH", [safePull(transferPushQueue_q)])
		return True
	else:
		return False

def terminal(option, pullString_q, pushString_q):
	if option == 0:
		clientTerminal(pullString_q, pushString_q)
		return True
	else:
		return False