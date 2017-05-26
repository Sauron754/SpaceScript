import SpaceScript
import multiprocessing
from SpaceScript import frontEnd
from SpaceScript.frontEnd import terminal as terminal

def simThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):


def termThread(queues_arr, pipes_arr, holdValue_v, objectArray_arr, mainLock):
	initialized_bool = True
	lowTermThreadHold_v = multiprocessing.Value("i")
	messageQueue_q = queues_arr[0]

	while initialized_bool:
		message = messageQueue_q.get()
		IOThread = multiprocessing.Process(target = lowTermThread, args = ())
		
def lowTermThread(outString_str, mode_int, parentHoldValue_v, stringPipe_p):
	inString_str = terminal(mode_int, outString_str)
	stringPipe_p.send(inString_str)
	parentHoldValue_v.value = 1
	return inString_str