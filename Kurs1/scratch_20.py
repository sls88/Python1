s=[]
ssr=[]
b1=0
b2=0
b3=0
with open("D:\\1.txt", "r") as file:
    for i in file:
        i=[i.strip().split(";")]
        s+=i
    for k in s:
        jj=(int(k[1])+int(k[2])+int(k[3]))/3
        ssr+=[jj]
    for p in s:
        b1+=int(k[1])
        b2+=int(k[2])
        b3+=int(k[3])
print(s)
with open("D:\\2.txt",'w') as out:
    for u in ssr:
        out.write(str(u)+"\n")
    out.write(str(b1/len(s)/4) + " "+str(b2/len(s)/4) + " "+ str(b3/len(s)/4) + " ")
