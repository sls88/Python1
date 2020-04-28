k=0
i=0
while i<5:
    a,b=input("Пиши через пробел: ").split(" ")
    a = int(a)
    b = int(b)
    if a==0 and b==0:
        break
    elif a==0 or b==0:
        if a==0 and b!=0:
            k+=b
        elif a!=0 and b==0:
            k+=a
        continue
    print(a*b)
    k+=(a*b)
    i+=1
print(k)

