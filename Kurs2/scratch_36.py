n, k = map(int, input().split())
def razl(n, k):
    if k==0:
        return 1
    elif k>n:
        return 0
    else:
        p=razl(n-1,k)+razl(n-1,k-1)
        return p
print(razl(n, k))