import SpaceScript
import multiprocessing
from multiprocessing import Process, Queue, Pipe, Lock
from SpaceScript import frontEnd
from SpaceScript import utility
from SpaceScript.frontEnd import terminal
from SpaceScript.utility import terminalUtility
from SpaceScript.terminal import terminal as terminal
from SpaceScript.utility.terminalUtility import safePull as safePull
from SpaceScript.utility.terminalUtility import termThreadEventHandler as termThreadEventHandler
from SpaceScript.utility.terminalUtility import termThreadControlHandler as termThreadControlHandler
from appJar import gui

def simThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr = None,
			  mainLock = None):


def termThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr = None,
			   mainLock = None):
	commandPipe = pipes_arr[0]
	controlQueue_q = queues_arr[0]
	pullString_q = multiprocessing.Queue()
	pushString_q = multiprocessing.Queue()
	termThreadHold_v = multiprocessing.Value()
	guiHold_v = multiprocessing.Value()
	guiHold_v.value = False
	termThreadHold_v.value = False
	subProcess = multiprocessing.Process(target = terminal, args = (0,
										pullString_q, pushString_q,
										guiHold_v, termThreadHold_v))
	subProcess.start()
	checkSequence_bool = True
	while checkSequence_bool:
		termThreadEventHandler(termThreadHold_v, pullString_q, commandPipe,
							   holdValue_v)
		termThreadControlHandler(termThreadHold_v, controlQueue_q, pushString_q,
								 guiHold_v)