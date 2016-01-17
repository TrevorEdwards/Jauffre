import command

command_list = ["joke","weather","music","light"]

def interpret(s):
	for cmd in command_list:
		if s.find(cmd) != -1:
			command.Command(cmd).do()
			return
