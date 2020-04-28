s=[]
ssr=[]
shag=0
ball=0
vsego=0
b1=0
b2=0
b3=0
with open("D:\\1.txt", "r") as file:
    for i in file:
        i=i.strip().split(";")
        s+=i
    for j in range(len(s)-4,-1, -4):
        del s[j]
    for k in s:
        ball+=int(k)
        shag+=1
        if shag==3:
            ssr+=[int(ball)/3]
            shag = 0
            ball = 0
    for p in s:
        vsego +=1
        shag +=1
        if shag==1:
            b1+=int(p)
        elif shag==2:
            b2+=int(p)
        elif shag == 3:
            b3+=int(p)
            shag = 0
    else:
        b1/=vsego/3
        b2/=vsego/3
        b3/=vsego/3
with open("D:\\2.txt",'w') as out:
    for u in ssr:
        out.write(str(u)+"\n")
    out.write(str(b1) + " "+str(b2) + " "+ str(b3) + " ")

