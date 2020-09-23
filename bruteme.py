import os
import sys
import threading
import time

from optparse import OptionParser

# Plugin
from plugin.zip import Zip
from plugin.rar import Rar
from plugin.ssh import SSH

class BruteMe:
    def __init__(self):
        self.opt = None
        self.args = None
        self.log = None
        self.word = []
        self.user = []
        self.pasw = []

    def readWordlist(self):
        if self.opt.wordlist:
            if os.path.isfile(self.opt.wordlist):
                if self.opt.byte:
                    openFile = open(self.opt.wordlist, "rb").read()
                    print ("[!] Converting bytes to strings")
                    count = 0
                    total = len(openFile.splitlines())
                    error = False
                    for word in openFile.splitlines():
                        if word == " ":
                            if count > 1:
                                print ()
                            print ("[!] Line empty -> skip")
                        else:
                            try:
                                count += 1
                                self.word.append(word.decode())
                                if self.log:
                                    print ("\r[*] Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                            except UnicodeDecodeError:
                                if self.log:
                                    print ()
                                i = input("\r[!] Program can't read the bytes, continue? (Y/n): ")
                                if i != "y" or i != "Y":
                                    error = True
                                    break
                                else:
                                    continue
                    if error == False and self.log:
                        print ("")
                else:
                    try:
                        openFile = open(self.opt.wordlist, "r").read()
                        count = 0
                        for word in openFile.splitlines():
                            if word == " ":
                                if count > 1:
                                    print ()
                                print ("[!] Line empty -> skip")
                            else:
                                count += 1
                                self.word.append(word)
                                if self.log:
                                    print ("\r[*] Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                        if self.log:
                            print()
                    except UnicodeDecodeError:
                        print ("[!] Failed to read the file, please use '-b' to change to byte mode")
                        sys.exit()

                print ("[*] Done, total word: %d" % (count))
            else:
                print ("[!] File '%s' has been found" % (self.opt.wordlist))
        else:
            print ("[!] Wordlist must be set")
            sys.exit()

    def readUserPass(self):
        if self.opt.user and self.opt.pasw:
            if os.path.isfile(self.opt.user) != True:
                print ("[!] File '%s' has been not found" % (self.opt.user))
                sys.exit()
            if os.path.isfile(self.opt.pasw) != True:
                print ("[!] File '%s' has been not found" % (self.opt.pasw))
                sys.exit()

            if self.opt.byte:
                    openFile = open(self.opt.user, "rb").read()
                    print ("[!] User: Converting bytes to strings")
                    count = 0
                    total = len(openFile.splitlines())
                    error = False
                    for word in openFile.splitlines():
                        if word == " ":
                            if count > 1:
                                print ()
                            print ("[!] User: Line empty -> skip")
                        else:
                            try:
                                count += 1
                                self.user.append(word.decode())
                                if self.log:
                                    print ("\r[*] User: Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                            except UnicodeDecodeError:
                                if self.log:
                                    print ()
                                i = input("\r[!] User: Program can't read the bytes, continue? (Y/n): ")
                                if i != "y" or i != "Y":
                                    error = True
                                    break
                                else:
                                    continue
                    if error == False and self.log:
                        print ("")

                    openFile = open(self.opt.pasw, "rb").read()
                    print ("[!] Pass: Converting bytes to strings")
                    count = 0
                    total = len(openFile.splitlines())
                    error = False
                    for word in openFile.splitlines():
                        if word == " ":
                            if count > 1:
                                print ()
                            print ("[!] Pass: Line empty -> skip")
                        else:
                            try:
                                count += 1
                                self.pasw.append(word.decode())
                                if self.log:
                                    print ("\r[*] Pass: Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                            except UnicodeDecodeError:
                                if self.log:
                                    print ()
                                i = input("\r[!] Pass: Program can't read the bytes, continue? (Y/n): ")
                                if i != "y" or i != "Y":
                                    error = True
                                    break
                                else:
                                    continue
                    if error == False and self.log:
                        print ("")
            else:
                    try:
                        openFile = open(self.opt.user, "r").read()
                        count = 0
                        for word in openFile.splitlines():
                            if word == " ":
                                if count > 1:
                                    print ()
                                print ("[!] User: Line empty -> skip")
                            else:
                                count += 1
                                self.user.append(word)
                                if self.log:
                                    print ("\r[*] User: Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                        if self.log:
                            print()
                    except UnicodeDecodeError:
                        print ("[!] User: Failed to read the file, please use '-b' to change to byte mode")
                        sys.exit()
                    except TypeError:
                        print ("[!] User: Failed to read the file, please use '-b' to change to byte mode")
                        sys.exit()

                    try:
                        openFile = open(self.opt.wordlist, "r").read()
                        count = 0
                        for word in openFile.splitlines():
                            if word == " ":
                                if count > 1:
                                    print ()
                                print ("[!] Pass: Line empty -> skip")
                            else:
                                count += 1
                                self.pasw.append(word)
                                if self.log:
                                    print ("\r[*] Pass: Reading the file, please wait... ~> %d" % (count), end="", flush=True)
                        if self.log:
                            print()
                    except UnicodeDecodeError:
                        print ("[!] Pass: Failed to read the file, please use '-b' to change to byte mode")
                        sys.exit()
                    except TypeError:
                        print ("[!] User: Failed to read the file, please use '-b' to change to byte mode")
                        sys.exit()
            print ("[*] Done, total word: %d" % (count))    
        else:
            print ("[!] User or Pass must be set")
            sys.exit()

    def parseArgs(self):
        if self.opt.mode:
            if self.opt.mode == "zip":
                self.readWordlist()
                if self.opt.file:
                    pass
                else:
                    print ("[!] Files are needed, please set the file location!")
                    sys.exit()
                zip = Zip()
                zip.setWord(self.word)
                zip.setLog(self.log)
                zip.setFile(self.opt.file)
                zip.crack()
            elif self.opt.mode == "rar":
                self.readWordlist()
                if self.opt.file:
                    pass
                else:
                    print ("[!] Files are needed, please set the file location!")
                    sys.exit()
                rar = Rar()
                rar.setWord(self.word)
                rar.setLog(self.log)
                rar.setFile(self.opt.file)
                rar.crack()
            elif self.opt.mode == "ssh":
                self.readUserPass()
                
                ssh = SSH()
                ssh.setHostPort(self.opt.hostname)
                ssh.setTimeout(self.opt.timeout)
                ssh.setLog(self.log)
                ssh.setUser(self.user)
                ssh.setPass(self.pasw)
                ssh.crack()
        else:
            print ("[!] Mode required")
            sys.exit()

    def checkIsRequired(self):
        data = []
        if self.opt.mode:
            data.append({"Mode": "ok"})
        if self.opt.wordlist:
            data.append({"Wordlist": "ok"})
        if self.opt.file:
            data.append({"File": "ok"})
        if self.opt.byte:
            data.append({"Use Byte mode": "ok"})
        if self.opt.logs:
            data.append({"Using Log": "ok"})
        if self.opt.user:
            data.append({"Username": "ok"})
        if self.opt.pasw:
            data.append({"Password": "ok"})
        if self.opt.hostname:
            data.append({"Hostname": "ok"})
        if self.opt.timeout:
            data.append({"timeout": "ok"})
        if len(data) > 0:
            for dictData in data:
                for key in dictData:
                    if dictData[key] == "ok":
                        print ("[*] " + key + ": " + dictData[key])
            print ("-" * 20)
        else:
            print ("[-] Please input argument")

    def main(self):
        parser = OptionParser()
        parser.add_option("-m", "--mode", dest="mode", help="Set mode [zip,rar,hash]", action="store")
        parser.add_option("-w", "--wordlist", dest="wordlist", help="Set wordlist from file", action="store")
        parser.add_option("-f", "--file", dest="file", help="Set file", action="store")
        parser.add_option("-b", "--byte", dest="byte", help="Use encoding to read Wordlist", action="store_true")
        parser.add_option("-l", "--log", dest="logs", help="Show log", action="store_true")
        parser.add_option("-u", "--user", dest="user", help="Set username list", action="store")
        parser.add_option("-p", "--pass", dest="pasw", help="Set password list", action="store")
        parser.add_option("-t", "--target", dest="hostname", help="Set hostname", action="store")
        parser.add_option("--timeout", dest="timeout", help="Set timeout", action="store")
        self.opt, self.args = parser.parse_args()
        if self.opt.logs:
            print ("[!] Logs have been activated")
            self.log = True
        self.checkIsRequired()
        self.parseArgs()

if __name__ == "__main__":
    brute = BruteMe()
    brute.main()
