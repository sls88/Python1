p =""
sp1=""
s=[]
dict={}
with open("D:\\1.txt", "r")as a:
    for i in a:
        i=i.strip()
        p+=str(i+" ")
for j in p:
    if "A"<j<="z":
        sp1+=j
    elif " "==j:
        sp1=sp1.lower()
        s+=[sp1]
        sp1 = ""
word=""
l=s.count(s[0])
for h in s:
    if s.count(h)>=l:
        word = h
        l=s.count(h)
print(word, l)
