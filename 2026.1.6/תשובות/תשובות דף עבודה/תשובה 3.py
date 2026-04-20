max=0
richest=""
b=0
a="XXX"
while b<=0 or a=="xxx":
    a=(input("שם המורה"))
    b=int(input("משכורת"))
    if a=="עמית":
        print("יצאנו")
    if b>max:
        max=b
        richest=a
if richest!="":    
    print("המורה העשיר ביותר :",richest)
    print("עם משכורת של",max)
