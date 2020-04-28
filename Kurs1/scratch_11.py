def update_dictionary(d2,key,value):
    d=d2
    key1=key
    value1=value
    if d.get(key1)!=None:
        d[key1]+=[value1]
    else:
        if d.get(key1*2)!=None:
            d[key1*2]+=[value1]
        else:
            d[key1*2]=[value1]
    return d
a={}
print(update_dictionary(a,1,-1))
update_dictionary(a,1,-1)
print(a)
update_dictionary(a,2,-2)
print(a)