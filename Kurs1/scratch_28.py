d={}
sep1=set()
s=[]
n1= int(input())
for i in range(n1):
    a=str(input().lower())
    d[a]=a
n2 =int(input())
for j in range(n2):
    a=input().lower().split()
    s+=a
for k in s:
    if k not in d:
        sep1.add(k)
for l in sep1:
    print(l)