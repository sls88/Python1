ans=set()
for obj in objects:
    b=id(obj)
    ans.add(b)
print(len(ans))