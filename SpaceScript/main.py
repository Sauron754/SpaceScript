import SpaceSript
import multiprocessing
from SpaceScript import frontEnd
from SpaceScript import threadingFunctions
from SpaceScript.frontEnd import bashFunctions
from SpaceScript.threadingFunctions import simThread
from SpaceScript.threadingFunctions import termThread

controlQueue_q = multiprocessing.Queue()
promtCommandPipe_p = multiprocessing.Pipe()
mainHoldValue_v = multiprocessing.Value()
queues_arr = [controlQueue_q]
pipes_arr = [promtCommandPipe_p]
term = multiprocessing.Process(target = termThread, args = (queues_arr,
															pipes_arr,
															mainHoldValue_v))
term.start()