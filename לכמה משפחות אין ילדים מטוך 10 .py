v=0
c=0
for i in range  (1,11):
     a=int(input("כמה  ילדי"))
     if a==0:
         c=c+1
     if i==10 and a==10 :
        v=v+1
     
print(c,"כמות המשפחוט שאין להאם ילדים")     
if v==1:
    print("למשפחה 10 יש 10 ילדים")

