def clientTerminalIOTest():
	#this test sequence can only be executed by a human
	#therefore it is not included in the standardized testing procedure
	#if anything is modified in the terminal gui the dev working on it is asked
	#to verify the codes integrity himself
	import multiprocessing
	import SpaceScript
	from multiprocessing import Process, Queue, Value
	from SpaceScript import frontEnd
	from SpaceScript.frontEnd import terminal
	from SpaceScript.frontEnd.terminal import terminal as terminal
	pullQueue_q = multiprocessing.Queue()
	pushQueue_q = multiprocessing.Queue()
	holdValue_v = multiprocessing.Value('h')
	childHoldValue_v = multiprocessing.Value('h')
	thread = multiprocessing.Process(target = terminal, args = (0, pullQueue_q,
									 pushQueue_q, childHoldValue_v,
									 holdValue_v))
	print("You should now see this message displayed in the gui!")
	pushQueue_q.put("You should now see this message displayed in the gui")
	childHoldValue_v.value = True