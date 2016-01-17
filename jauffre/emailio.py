import poplib
import email
#from email import parser

def get():
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('jauffrebot')
    pop_conn.pass_('jauffredragon')
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message into an email object:
    #messages = [parser.Parser().parsestr(mssg) for mssg in messages]
    #for message in messages:
    #    print message
    pop_conn.quit()
    if len(messages) > 0:
        print messages[0]
        return messages[0]
