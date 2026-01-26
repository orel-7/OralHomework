a=0
b=0
c=0
d=0
e=0

f=int(input("הגרלה: "))

while f != -1:
    g=int(input("הופעה: "))
    h=int(input("מזנון: "))
    
    a=a+1
    b=b+f
    c=c+g
    d=d+h
    
    if f>10:
        e=e+1    
    f=int(input("הגרלה: "))
print("אנשים:", a)
print("סה''כ הגרלה:", b)
print("סה''כ הופעה:", c)
print("סה''כ מזנון:", d)
print("חינם:", e)