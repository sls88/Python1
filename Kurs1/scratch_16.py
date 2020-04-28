with open("D:\\1.txt", "r") as r:
    a=r.readline()
    itog=""
    number=""
    litter=""
    for i in range(0,len(a)-1):
        if a[i]<"A":              # Цифры
            if a[i+1]<"A":
                number+=a[i]
                if i == len(a) - 2:
                    number += a[i+1]
                    number = int(number)
                    itog += litter * number
            elif a[i+1]>="A":
                number+=a[i]
                number=int(number)
                itog+=litter*number
                number = ""
                litter = ""
        elif a[i]>="A":              # Буквы
            litter+=a[i]
            if i==len(a)-2:
                number += a[i+1]
                number = int(number)
                itog += litter * number
with open("D:\\2.txt", "w") as b:
    b.write(itog)