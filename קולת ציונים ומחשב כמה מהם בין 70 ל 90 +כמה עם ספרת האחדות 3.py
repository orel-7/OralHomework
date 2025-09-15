A=0
B=0
for i in range(10):
    c=int(input("ציון"))
    if 70<=c<=90:
        A=A+1
    if c % 3 == 0:
        B=B+1
    
print("מספר הציוניים בין 70 ל90 ",A)
print(B)    


