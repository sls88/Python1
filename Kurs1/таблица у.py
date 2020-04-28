a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a<=b and c<=d and b<=10 and a<=10 and c<=10 and d<=10:
    print("\t",end="")
    for i in range(c,d+1):
        print(i, end="\t")
    print()
    for j in range(a,b+1):
        print(j, "\t", end="")
        for k in range(c,d+1):
            k=k*j
            print(k, end="\t")
        print()
else:
    print('Введите корректные данные')