A = 0   
B = 0   
for i in range(10):
    c=int(input("הכנס ציון: "))
    if c%2==0:
        A+=1
    if c%10==8:
        B+=c
print("כמות מספרים זוגיים:", A)
print("סכום מספרים שמסתיימים ב-8:", B)
