import SpaceScript
import multiprocessing
from SpaceScript import frontEnd
from SpaceScript.frontEnd import terminal as terminal

def simThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):


def termThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):
	initialized_bool = True
	initializedInnerLoop_bool = True
	lowTermThreadHold_v = multiprocessing.Value("i")
	lowTermStringPipeRecv_p, lowTermStringPipeSend_p = multiprocessing.Pipe(
		duplex = True)
	messageQueue_q = queues_arr[0]

	while initialized_bool:
		while initializedInnerLoop_bool:
			
			IOThread = multiprocessing.Process(target = lowTermThread, args = (
				outString_str, IOMode_int, lowTermThreadHold_v,
				lowTermStringPipeSend_p))

		
def lowTermThread(outString_str, mode_int, parentHoldValue_v, stringPipe_p):
	inString_str = terminal(mode_int, outString_str)
	stringPipe_p.send(inString_str)
	parentHoldValue_v.value = 1
	return inString_str