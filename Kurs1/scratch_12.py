def f(x):
    return x+2
cache = {}

for _ in range(int(input())):
    x = int(input())
    if x not in cache:
        cache[x] = f(x)

    print(cache[x])