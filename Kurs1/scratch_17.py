p = []
with open("D:\\1.txt", "r")as a:
    for i in a:
        i=i
        p+=[i]
print(p)
v = []
for f in range(10):
    t="D:\\1\ "
    l=".exe"
    s=str(f)
    k=t+s+l
    print(k)
    with open(k, "w")as out:
        for j in p:
            out.write(j+"\n")