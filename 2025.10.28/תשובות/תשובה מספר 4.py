b1=0
b2=0
d=0
a1=0
a2=0
aaa=0
for i in range (10):
    a=int(input("ציון")) 
    if 0<i>=5:
        b1=b1+a
    if 5<i>=10:
        b2=b2+a
    if 0<i>=5 and a%2==0:
        d=d+1
    if i==1:
        a1=a
    if i==10:
        a2=a
    if i==2 and a==80:
        aaa=1
if b1==b2:
    print("סכום הציוניים 1-5 ו5-10 שווים ")

if d==5:
    print("הציונים 5 הרשוניים זוגעיים")

if aaa==1:
    print("המסרהשני שווה 80")
if a1==a2:
    print("הציון הראשון והאחרון שווים אחד לשני")

if a1==a2:
    print("הציון האחרון שווה למיון הראשון")
