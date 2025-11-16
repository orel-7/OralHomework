z=0
e=0
for i in range (10):
    a=int(input("ציוניים"))

    if a%2==0:
        z=z+1
    else:
        e=e+1 
    if z>e:
        print("יש יותר ציונים זוגיים")
    else:
     if e>z:
        print("יש יותר ציונים אי זוגיים")
     else:
        print("יש אותו מספר ציונים זוגיים ואי זוגיים")

    if i==6 or i== 7 or i==8 or i==9 or i==10:
        print("שלום")