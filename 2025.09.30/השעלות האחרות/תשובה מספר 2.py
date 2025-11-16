B=0
for i in range(10):
    A=int(input("ציון"))
    print(A%10)
    if A%10==8:
        B=B+1
print(B)