def clientTerminal(out_str):
	print(out_str)
	command_str = input()
	return command_str
def terminal(option_int, out_str = 'none'):
	if option_int == 0:
		if out_str == 'none':
			command_str = clientTerminal('Welcome to SpaceScript!!!')
		else:
			command_str = clientTerminal(out_str)
		return command_str