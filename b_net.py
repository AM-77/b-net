from pexpect import pxssh
import getpass

class Bot:
    def __init__(self, host, uname, pswd):
        self.host = host
        self.uname = uname
        self.pswd = pswd
        self.session = self.ssh()

    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.uname, self.pswd)
            return bot
        except:
            print('[!] There was an error in login')

    def send_cmd(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


botnets = []
def add_bot(host, uname, pswd):
    botnets.append(Bot(host, uname, pswd))

def execute_cmd(cmd):
    for bot in botnets:
        send = bot.send_cmd(cmd)
        print('[+] Bot: ' + bot.uname + '@' + bot.host + '$ ' )
        print(send)


while True:
	print("Adding new bot: \n")
	host = raw_input("\thostname: ")
	uname = raw_input("\tusername:  ")
	pswd = getpass.getpass("\tpassword: ")

	add_bot(host, uname, pswd)
	
	print("new bot was added successfully.\n")
	respond = raw_input("\tadd new bot ? y/n ? : ")

	if(respond == "y" || respond == "Y"):
		break

while True:
	command = raw_input(">>$ ")
	execute_cmd(command)
