def modify_list(l):
    l+=[]
    a=[len(l)]
    for i in range(len(l)-1,-1,-1):
        l[i]=int(l[i])
        if l[i]%2==0:
            l[i]=int(l[i]/2)
        elif l[i]%2!=0:
            del l[i]
    return l
print(modify_list(lsj))
lst=[1,2,3,4,5,6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)
lst=[10,5,8,3]
modify_list(lst)
print(lst)


for key in d:
    if key == key1:
        d[key1] += [value1]
    else:
