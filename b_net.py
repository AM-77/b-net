from pexpect import pxssh

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


