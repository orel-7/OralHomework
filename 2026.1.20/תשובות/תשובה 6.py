op2=0
a=input("מחרוזת ")
print(a.count("*"))
for i in range(0,len(a)):
    if a[i]=="*":
        op2=op2+1
print(op2)