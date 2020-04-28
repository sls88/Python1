a=str(input())
b=str(input())
s=[]
s+=a+b
sinv=[]
sinv+=b+a
d={}
d2={}
for i in range(0,int(len(s)/2)):
    d[s[i]]=s[int(len(s)/2)+i]
x=str(input())
z=str(input())
s2=[]
s2+=x
for j in s2:
    print(d[j], end="")
print()
s3=[]
s3+=z
for p in range(0,int(len(sinv)/2)):
    d2[sinv[p]]=sinv[int(len(sinv)/2)+p]
for k in s3:
    print(d2[k], end="")