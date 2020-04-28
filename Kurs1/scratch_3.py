s=str(input())
k=0
n=0
if (len(s))==1:
    print(s[0], end="")
    print(1, end="")
for j in range(k,len(s)-1):
    k+=1
    if s[k-1] == s[k]:
        n+=1
        if k==(len(s)-1):
            print(s[k], end="")
            print(n+1, end="")
    elif s[k-1] != s[k]:
        if k==(len(s)-1):
            print(s[k-1], end="")
            print(n+1, end="")
            print(s[k], end="")
            print(1, end="")
        else:
            print(s[k-1], end="")
            print(n+1, end="")
            n=0
