b=0 # סופר כמה דנה יש בשמות
d=0 #האם אחד מהאוטיות שם 
c=0 #כמה שמות יותר מ7 תויים 
for i in range(7):
    a=input("neame")
    if "דנה" in a:
        b=b+1
    print(a[-1])
    if len(a)>7:
        c=c+1
    if "א" in a or "י"in a or "ה"in a or "ו"in a :
        d=d+1
print("כמות השמות שיש יותר מ7 תווים ",c)      
print("כמות השמות שמכילים ",d)
print("כמות השמות שנקלתו העונים לשם דנה ",b)