import SpaceScript
import multiprocessing
from SpaceScript import frontEnd
from SpaceScript import utility
from SpaceScript.frontEnd import terminal as terminal
from SpaceScript.utility import terminalUtility
from SpaceScript.utility.terminalUtility import safePull as safePull

def simThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):


def termThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):
	initialized_bool = True
	lowTermThreadHold_v = multiprocessing.Value("i")
	lowTermStringPipeRecv_p, lowTermStringPipeSend_p = multiprocessing.Pipe(
		duplex = True)
	messageQueue_q = queues_arr[0]
	commandPipe_p = pipes_arr[0]

	while initialized_bool:
		initializedInnerLoop_bool = True
		while initializedInnerLoop_bool:
			lowTermThreadHold_v.value = 0
			outString_str = safePull(messageQueue_q)
			IOThread = multiprocessing.Process(target = lowTermThread, args = (
				outString_str, IOMode_int, lowTermThreadHold_v,
				lowTermStringPipeSend_p))
			while returnStatus == False:
				if lowTermThreadHold_v.value == 1:
					returnStatus == True
					holdValue_v.value = 1
					inString_str = lowTermStringPipeRecv_p.recv()
					commandPipe_p.send()


		
def lowTermThread(outString_str, mode_int, parentHoldValue_v, stringPipe_p):
	inString_str = terminal(mode_int, outString_str)
	parentHoldValue_v.value = 1
	stringPipe_p.send(inString_str)
	return inString_str