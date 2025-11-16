for i in range(10):
    b=int(input("הכנס מספר "))
    
    if b%2==0:
        print("     ")
    else:
        if 100 <= b <= 999:
            print("ספרת האחדות",b%10)
            print("ספרת המאות",b//100)
            print("סכום הספרות",(b%10)+(b//100))
