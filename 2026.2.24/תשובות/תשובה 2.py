b=0
c=0
a=int(input("מספר "))
while b==0:
    if a%2==0:
        b=b+1
    else:
        c=c+1
print("כמות הזוגים",b)
print("כמות האי זוגים",c)