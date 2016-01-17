import command

command_list = ["joke","weather","play","pause","stop","skip","light","security"]

def interpret(s):
	print "meow"
	for cmd in command_list:
		if s.find(cmd) != -1:
                        print cmd
			return command.Command(cmd).do()
