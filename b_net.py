#!/usr/bin/python3

from pexpect import pxssh
import getpass
from os import system, name
import sys

b_net = """ 


      ..                                           s    
. uW8"                                            :8    
`t888                   u.    u.                 .88    
 8888   .             x@88k u@88c.      .u      :888ooo 
 9888.z88N           ^"8888""8888"   ud8888.  -*8888888 
 9888  888E            8888  888R  :888'8888.   8888    
 9888  888E            8888  888R  d888 '88%"   8888    
 9888  888E            8888  888R  8888.+"      8888    
 9888  888E 88888888   8888  888R  8888L       .8888Lu= 
.8888  888" 88888888  "*88*" 8888" '8888c. .+  ^%888*   
 `%888*%"               ""   'Y"    "88888%      'Y"    
    "`                                "YP'              
                                                        
                                                        
                                                        

"""
 
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
        data = bot.send_cmd(cmd)
        print('[+] Bot: ' + bot.uname + '@' + bot.host + '$ ' + data.decode() )

def clear():   
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


print(b_net)
while True:
	print("[+] Adding new bot:")
	host = input("\thostname: ")
	uname = input("\tusername: ")
	pswd = getpass.getpass("\tpassword: ")

	add_bot(host, uname, pswd)
	
	print("[+] New bot was added successfully.\n")
	respond = input("[?] Add new bot ? y/n ? : ")

	if(respond == "n" or respond == "N"):
		break
		
print(b_net)
while True:
    try:
        command = input(">>$ ")
        execute_cmd(command)
    except KeyboardInterrupt :
        print('\nBye.')
        sys.exit()   
        
