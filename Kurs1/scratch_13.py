with open("D:\контакт.txt", "w") as inf:
    n=int(input())
    for i in range(n+1):
        inf.write(str(i))
        inf.write(str("\n"))