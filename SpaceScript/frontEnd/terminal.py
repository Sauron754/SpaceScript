def clientTerminal(out_str):
	

def terminal(option_int, out_str = chr(0)):
	if option_int == 0:
		if out_str == chr(0):
			command_str = clientTerminal('Welcome to SpaceScript!!!')
		else:
			command_str = clientTerminal(out_str)
		return command_str
