import requests
with open("D:\\1.txt", 'r')as inf:
    inf=inf.readline().strip()
r=requests.get(inf)
k=[]
k+=r.text.splitlines()
with open("D:\\2.txt", "w")as ouf:
    for i in k:
        ouf.write(str(i)+"\n")
h=0
for p in k:
    h+=1
print(h)
print(*p)