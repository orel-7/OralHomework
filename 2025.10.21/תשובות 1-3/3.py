a=int(input("כמה חולצות קנה רמי"))
b=int(input("כמה עולה כל חולצה"))
c=a*b
if c > 100:
    d=100+(c-100)*0.5
else:
    d=c
print("עליך לשלם ",d)