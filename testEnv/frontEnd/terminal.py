def clientTerminalIOTest():
	#this test sequence can only be executed by a human
	#therefore it is not included in the standardized testing procedure
	#if anything is modified in the terminal gui the dev working on it is asked
	#to verify the codes integrity himself
	import multiprocessing
	import SpaceScript
	from multiprocessing import Processing, Query, Value
	from SpaceScript import frontEnd
	from SpaceScript.frontEnd import terminal
	pullQueue_q = multiprocessing.Query()
	pushQueue_q = multiprocessing.Query()
	holdValue_v = multiprocessing.Value()
	childHoldValue_v = multiprocessing.Value()