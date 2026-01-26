max_h = 0
top_n = ""
c=int(input("כמה תלמידים יש ?"))
for i in range (c):
    n=input("הכנס שם: ")
    h=float(input("הכנס גובה: "))
    while n != "ישראל" and h != 1.80:
        if h>max_h:
            max_h=h
            top_n=n
    n=input("הכנס שם: ")
    h=float(input("הכנס גובה: "))

    if top_n != "":
        print("התלמיד הכי גבוה הוא:", top_n)
        print("בגובה:", max_h)
    else:
        print("לא הוזנו נתונים")