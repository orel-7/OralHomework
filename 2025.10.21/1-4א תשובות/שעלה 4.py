for i in range(100):
    a=int(input("הכנס קוד "))
    b=int(input(" ממוצע ציוני בגרות "))
    if a==1:
        print(" בפקולטה לרפואה")
    if a==2:
        print(" בפקולטה למשפטים")
    if a==3:
        print("במדעי הרוח")
    else:
        if a!=1 and a!=2 and a!=3:
            print("קוד לא תקין")
    
    print(100-b,"נקודות להגיע למאה")











