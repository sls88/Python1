a=[int(i) for i in input().split()]
a.sort()
for i in range(0, len(a)):
    if a[i]==a[len(a)]:
        if a[len(a)]==a[len(a)-1]:
            print(a[len(a)], end=" ")
    elif a[i]==a[i+1]:
        if a[i]!=
        print(a[i+1], end=" ")
    elif a[i]!=a[i+1]:
        del a[i+1]
    print(a[i], end=" ")
