b=0
c=0
d=0
for i in range(100):
    a=int(input("הכנס מספר "))
    if i<=1 and i>=10:
       b=b+a
    if i<=90 and i>=100:
        c=c+a
    if i!=5 or i!=9:
        d=d+a
print("סכום המספריים בין 1-10",b)
print("סכום ה10 האחורניים",c)
print("סכום כל המספריים השוניים מ5 או 3",d)