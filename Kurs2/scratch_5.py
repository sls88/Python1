from simplecrypt import *
with open("C:\\Myproject1\\test1\\encrypted.bin", "rb") as inp:
    l = inp.read()
s=[]
with open("C:\\Myproject1\\test1\\passwords.txt", "r") as passs:
    for line in passs:
        a=line.replace('\n', '')
        s.append(a)
for i in s:
    try:
        p=decrypt(i,l)
        print(p.decode("utf-8"))
        break
    except DecryptionException:
        continue