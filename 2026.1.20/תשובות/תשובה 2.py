a=input("מחרוזת ")
b=a.count("*")
c=a.count("?")
print("כמות ה*",b)
print("כמות סימני שעלה ",c)
if b<c:
    print("יש יותר סמני שעלה ")
else:
    print("יש יותר כוביות")