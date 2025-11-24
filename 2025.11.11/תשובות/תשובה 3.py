d=0
c=0
for i in range(10):
    a=int(input(" מספר ראשון"))
    b=int(input("מספר שני"))
    if i<=1 and i<=5:
        d=d+a+b
    if a<b:
        print("המספר הקטן ",a)
        c=c+a
    else:
        print("המספר הקטן",b)
        c=c+b
print("סכום המספרים הקטנים שהדפסת ",c)
print("סכום 5 מספרים הראשוניים",d)