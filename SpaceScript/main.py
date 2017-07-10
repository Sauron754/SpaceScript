import SpaceSript
import multiprocessing
from SpaceScript import frontEnd
from SpaceScript import threadingFunctions
from SpaceScript import utility
from SpaceScript.frontEnd import commandLineFunctions as commandLineFunctions
from SpaceScript.threadingFunctions import simThread as simThread
from SpaceScript.threadingFunctions import termThread as termThread
from SpaceScript.utility import terminalUtility
from SpaceScript.utility.terminalUtility import safePull as safePull
from multiprocessing import Queue, Pipe, Value

global controlQueue_q
global promtCommandPipe_p
global mainHoldValue_v
controlQueue_q = multiprocessing.Queue()
promtCommandPipe_p = multiprocessing.Pipe()
mainHoldValue_v = multiprocessing.Value()
queues_arr = [controlQueue_q]
pipes_arr = [promtCommandPipe_p]
term = multiprocessing.Process(target = termThread, args = (queues_arr,
															pipes_arr,
															mainHoldValue_v))
term.start()
loopActive = True
while loopActive:
	if mainHoldValue_v.value:
		if promtCommandPipe_p.poll():
			command_arr = promtCommandPipe_p.recv()
			function = getattr(commandLineFunctions, command_arr[0])
			function(command_arr[1])
			mainHoldValue_v.value = False
		else:
			mainHoldValue_v.value = False