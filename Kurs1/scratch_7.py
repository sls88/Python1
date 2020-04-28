a=[int(i) for i in input().split()]
b=[int(input())]
c=[]
for i in range(len(a)):
    if b[0]==a[i]:
        c+=[i]
if c==[]:
    print("Отсутствует")
c.sort()
print(*c, end=" ")