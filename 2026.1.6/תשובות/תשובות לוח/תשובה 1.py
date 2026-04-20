a=0
b=0
c=0
code=4
while code==0:
    code=int(input("קוד"))
    if code==1:
        a=a+1
    if code==2:
        b=b+1
    if code==3:
        c=c+1
print("כמות הילדים שנוסים באופניים",a)
print("כמות הילדים שנוסים באוטובוס",b)
print("כמות הילדים שהולכים ברגל",c)
