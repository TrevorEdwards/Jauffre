import command

command_list = ["joke","weather","play","pause","stop","skip","light"]

def interpret(s, runner):
	print "meow"
	for cmd in command_list:
		if s.find(cmd) != -1:
                        print cmd
			command.Command(cmd).do()
			return
