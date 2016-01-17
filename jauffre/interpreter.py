import command

command_list = ["joke","weather","play","pause","stop","skip","light"]

def interpret(s):
	for cmd in command_list:
		if s.find(cmd) != -1:
			command.Command(cmd).do()
			return
