from appJar import gui
from multiprocessing import Queue

def clientTerminal(pullString_q, pushString_q, holdValue_v):
	global term
	global transferQueue_q
	global transferHold_v
	transferHold_v = holdValue_v
	transferQueue_q = pullString_q
	term = gui()
	term.addListBox("mainOutput", ["Big thank you to appJar", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "", "Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>", "For more information type license"])
	term.addEntry("BASH")
	term.enableEnter(submit)
	app.go()

def submit(key):
	inputString_str = term.getEntry("BASH")
	transferQueue_q.put(inputString_str)
	holdValue_v.value = True
	return True

def terminal(option, pullString_q, pushString_q):
	if option == 0:
		clientTerminal(pullString_q, pushString_q)
		return True
	else:
		return False