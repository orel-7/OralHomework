A=0
B=0
x=int(input("מספר"))
for i in range(x):
    n=int(input("הכנס מספר "))
    if n>54:
        A+=1

    if n<55:
        B+=1

print("דולים מ 54 ",A)
print("קטניים מ 55 ",B)

if A>B:
    print("יש יותר מספרים גדולים מ-54")
else:
     print("יש יותר מספרים קטנים מ-55")
    