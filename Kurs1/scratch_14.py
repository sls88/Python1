a=str(input())
d={}
a=a.lower()
probel=" "
p=""
for i in range(0,len(a)):
    if a[i]==probel:
        if d.get(p)!=None:
            d[p]=d.get(p)+1
        elif d.get(p)==None:
            d[p]=1
        p=""
    elif a[i]!=probel:
        if len(a)-1==i:
            p+=a[i]
            if d.get(p)!=None:
                d[p]=d.get(p)+1
            elif d.get(p)==None:
                d[p]=1
            p=""
        p+=a[i]
for key,value in d.items():
    print(key,value)
print(a)