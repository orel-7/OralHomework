sum=0
a=int(input("הכנס מחיר חוג אנגלית "))
for i in range(100):
    b=int(input("מספר החודשים עבורם  אתם מעונינים לשלם לחוג אנגלית"))
    c=a*b
    sum=sum+c
    print(c)
print("סך הכנסות",sum)
