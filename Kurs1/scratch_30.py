s=[]
with open("D:\\1.txt","r")as into:
    for h in into:
        h=h.strip().split()
        s+=[h]
s.sort()
d={1:"-",2:"-",3:"-",4:"-",5:"-",6:"-",7:"-",8:"-",9:"-",10:"-",11:"-"}
name_cl=int(s[0][0])
viter=0
sum_rost=0
for k in s:
    if int(k[0])==name_cl:
        viter += 1
        sum_rost += int(k[2])
    elif int(k[0])!=name_cl:
        d[name_cl]=float(sum_rost/viter)
        name_cl=int(k[0])
        viter = 1
        sum_rost = int(k[2])
d[name_cl]=float(sum_rost/viter)
for key,value in d.items():
    print(key, value)