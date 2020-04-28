import requests
with open("D:\\3.txt", 'r')as inf:
    inf=inf.readline().strip()
r=requests.get(inf)
s=r.text
while "We" not in s:
    l=requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+s)
    s=l.text
    print(s)

