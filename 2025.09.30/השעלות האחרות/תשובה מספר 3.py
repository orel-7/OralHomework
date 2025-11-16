B=0
for i in range(10):
    A=int(input("כמה פלאפלים קנית? "))
    T=A*15
    print("אתה צריך לשלם",T)
    if A>5:
        B=B+1
print(B)

