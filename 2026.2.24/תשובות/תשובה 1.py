r=0 #רווקים 1
n=0 #נשועי
k=0 #כרוש 3 
al=0 #אלמן
for i in range (10):
    a=int(input("קוד"))
    if a==1:
        r=r+1
    if a==2:
        n=n+1
    if a==3:
        k=k+1
    if a==4:
        al=al+1
print("כמות הרווקים",r)
print("כמות הנסעוים", n)
print("כומות הגורשים",k)
print("כמות אלמנים ",al)