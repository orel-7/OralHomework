a=input("מחרוזת")
print(a.count("avi"))
for i in range (0,len(a)):
    if a[i]=="*":
        print(a[i-1],"אות אחרונה בכל שם ")
        print(a[i-2],"האות אחת לפני האחרונה של כל המחרוזת")