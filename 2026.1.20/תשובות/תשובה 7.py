a=input("מחרוזת ")
print("כמות השמות :",a.count("."))#א
print("כמות השם דנה",a.count("דנה"))#ב
print(a.replace("דנה", "רמה")) #ג
names = a.split(".") #ד
for name in names:
    name=name.strip()  
    print("אות אחרונה בשם:",name[-1])