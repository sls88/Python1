a=[int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
elif len(a)==2:
    print(a[1]*2, end=" ")
    print(a[0]*2, end=" ")
else:
    for c in range(0,len(a)-1):
        print((a[c-1]+a[c+1]), end=" ")
        if c+1==len(a)-1:
            print((a[len(a)-2]+a[0]), end="")