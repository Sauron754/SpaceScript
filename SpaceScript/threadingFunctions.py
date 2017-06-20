import SpaceScript
import multiprocessing
from multiprocessing import Process, Queue, Pipe, Lock
from SpaceScript import frontEnd
from SpaceScript import utility
from SpaceScript.frontEnd import terminal as terminal
from SpaceScript.utility import terminalUtility
from SpaceScript.utility.terminalUtility import safePull as safePull
from SpaceScript.utility.terminalUtility import termThreadEventHandler as termThreadEventHandler
from appJar import gui

def simThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr = None,
			  mainLock = None):


def termThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr = None,
			   mainLock = None):
	commandPipe = pipes_arr[0]
	pullString_q = multiprocessing.Queue()
	pushString_q = multiprocessing.Queue()
	termThreadHold_v = multiprocessing.Value()
	termThreadHold_v.value() = False
	subProcess = multiprocessing.Process(target = terminal, args = (
										pullString_q, pushString_q,
										termThreadHold_v))
	subProcess.start()
	eventHandler_bool = False
	while False:
		termThreadEventHandler(termThreadHold_v, pullString_q, commandPipe,
							   holdValue_v)