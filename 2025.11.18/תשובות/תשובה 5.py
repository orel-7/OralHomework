for i in range(10):
    a=int(input("הכנס ציון "))
    if a%2==0:
        b=b+a
    else:
        c=c+a
print("סכום הזוגים",b)
print("סכום אי הזוגים",c)
if b>c:
    print("סכום הזוגים יותר גדול ")
else:
    print("סכום אי הזוגים יותר גדול ")
