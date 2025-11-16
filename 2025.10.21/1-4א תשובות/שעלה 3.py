for i in range(10):
    a=int(input(" מספר ראשון"))
    b=int(input("מספר שני"))
    if a<b:
        print("המספר הקטן ",a)
    else:
        print("המספר הקטן",b)
    if (a<b and a!=3) or (b<=a and b!=3):
        print("שנה - טובה")
    if a > b:
        print("ההפרש הוא",a-b)
    else:
        print("ההפרש הוא",b-a)






