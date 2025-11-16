b=0
b2=0
for i in range (10):
    a=int(input("ציון")) 
    print("אחדות",a%10)
    if 55<a:
        b=b+1
    else:
        b2=b2+1
if b<b2:
    print("המורה נותנת פסק זמן")        