def suka(a):
    a=a
    b=[]
    k=0
    c=[]
    while k<a:
        k+=1
        for i in range(k):
            b.append(k)
    for j in range(k):
        c+=[b[j]]
    return c
z=suka(15)
print(*z)