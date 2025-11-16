b=0
for i in range(10):
    a=int(input("כמה פיצות קניתה"))
    if a>10:
        b=b+1
    if i==1 or i==2 or i==3 or i==4 or i==5:
        print("שלום")
    print("עליכה לשלם ",a*30)
    
print("כמות הלקחות שקנו מעל 10 פיצות",b)
