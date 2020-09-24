# BruteMe (Brute Force for ME)
BruteMe is a very simple and easy to use hacking tool. BruteMe can run on the Linux operating system.

## How to install
This tool can only run on the Linux operating system
```
sudo apt-get install git python3
git clone https://github.com/billalxcode/bruteme
cd bruteme
python3 bruteme.py
```

## How to use
- Brute Force SSH
```
python3 bruteme.py -m ssh -u [user wordlist] -p [pass wordlist] -t [target/hostname]
python3 bruteme.py -m ssh -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88
python3 bruteme.py -m ssh -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88:22
```
- Brute Force RAR
```
python3 bruteme.py -m rar -w [wordlist] -f [file]
python3 bruteme.py -m rar -w wordlist/userpass.txt -f tests/rar/crackme.rar
```
- Brute Force ZIP
```
python3 bruteme.py -m zip -w [wordlist] -f [file]
python3 bruteme.py -m zip -w wordlist/userpass.txt -f tests/zip/crackme.zip
```
- Brute Force MYSQL
```
python3 bruteme.py -m mysql -u [user wordlist] -p [pass wordlist] -t [target/hostname]
python3 bruteme.py -m mysql -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88
python3 bruteme.py -m mysql -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88:3306
```
- Brute Force FTP
```
python3 bruteme.py -m ftp -u [user wordlist] -p [pass wordlist] -t [target/hostname]
python3 bruteme.py -m ftp -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88
python3 bruteme.py -m ftp -u wordlist/user.txt -p wordlist/pasw -t 192.168.43.88:21
```

## Thanks for using this tool :)

## License
[MIT](https://choosealicense.com/licenses/mit/)
