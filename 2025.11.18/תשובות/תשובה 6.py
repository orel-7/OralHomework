b=0
x=int(input("ציון X"))
for i in range(10):
    a=int(input("ציון"))
    if a != x:
        b=b+a
        c=c+1
print("כמות הציוניים השונים מX",c)
print("סכם את הציוונים שונים מX",b)