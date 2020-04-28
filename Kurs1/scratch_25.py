s1=[]
s2=[]
n=int(input())
for i in range(0,n):
    s1+=[input().split(";")]
for j in s1:
    if int(j[1])>int(j[3]):
        s2+=[[j[0], 1, 1, 0, 0, 3]]
        s2+=[[j[2], 1, 0, 0, 1, 0]]
    elif int(j[1])<int(j[3]):
        s2+=[[j[0], 1, 0, 0, 1, 0]]
        s2+=[[j[2], 1, 1, 0, 0, 3]]
    elif int(j[1]) == int(j[3]):
        s2 += [[j[0], 1, 0, 1, 0, 1]]
        s2 += [[j[2], 1, 0, 1, 0, 1]]
for h in s2:
    s2.sort()
name=s2[0][0]
a1=0
a2=0
a3=0
a4=0
a5=0
for h in s2:
    if h[0] == name:
        a1+=h[1]
        a2+=h[2]
        a3+=h[3]
        a4+=h[4]
        a5+=h[5]
    elif h[0] != name:
        print ((name+":"),a1,a2,a3,a4,a5)
        name=h[0]
        a1 = h[1]
        a2 = h[2]
        a3 = h[3]
        a4 = h[4]
        a5 = h[5]
else:
    print((name + ":"), a1, a2, a3, a4, a5)