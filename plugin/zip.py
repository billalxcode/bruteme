import os
import sys
import zipfile
from tqdm import tqdm

class Zip:
    def __init__(self):
        self.word = []
        self.log = False
        self.file = ""

    def showFle(self, info):
        i = input("[?] Show all file? (Y/n): ")
        if i.lower() == "y":
            print("\t   %-46s %12s" % ("File Name", "Size file"), file=None)
            count = 0
            for file in info:
                count += 1
                print("%d.\t %-46s %12d" % (count, file.filename, file.file_size), file=None)

    def deleteFile(self, info):
        for file in info:
            os.remove(file.filename)

    def crack(self):
        count = 0
        found = False
        zip = zipfile.ZipFile(self.file, "r")
        for word in tqdm(self.word, total=len(self.word), unit="word"):
            try:
                zip.extractall(pwd=word.strip().encode())
            except:
                pass
            else:
                found = True
                break

        if found != True:
            print ("[!] Password not found")
            self.deleteFile(zip.infolist())
            zip.close()
        else:
            print ("[*] Password found: %s " % (word.strip()))
            self.showFle(zip.infolist())
            self.deleteFile(zip.infolist())
            zip.close()

    def setWord(self, word):
        self.word = word
        if self.log:
            print ("[*] The wordlist has been read")

    def setLog(self, type):
        self.log = type

    def setFile(self, path):
        if os.path.isfile(path):
            if self.log:
                print ("[!] File '%s' has been found" % (path))

            if zipfile.is_zipfile(path) != True:
                print ("[!] The file you entered is not a zip file")
                sys.exit()
            self.file = path
        else:
            print ("[!] File '%s' not found")
            sys.exit()
