s=[]
x=0
y=0
for i in range(int(input())):
    a=[input().lower().split()]
    s+=a
for j in s:
    if j[0]=="север":
        y+=int(j[1])
    elif j[0] == "юг":
        y -= int(j[1])
    elif j[0] == "запад":
        x -= int(j[1])
    elif j[0] == "восток":
        x += int(j[1])
print(x, y, end=" ")