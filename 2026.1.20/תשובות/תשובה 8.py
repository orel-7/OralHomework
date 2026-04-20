count=0
for i in range(10):
    s=input("הכנס מחרוזת: ")
    if "*"in s or"?"in s or"!"in s or"#"in s:
        count += 1
print(count)