def f(x):
    return x+2
d={}
k=[]
n=int(input())
for i in range(n):
    xi=int(input())
    if d.get(xi)!=None:
        k+=[d[xi]]
    elif d.get(xi)==None:
        d[xi]=f(xi)
        k+=[d[xi]]
for j in k:
    print(j)