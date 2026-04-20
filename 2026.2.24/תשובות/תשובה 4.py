b=0
for i in range (10):
    a=input("שם")
    print(a[len(a)-1])
    if a[0]=="א":
        b=b+1
    for i in range(5):
        print(a)
print("כמות השמות שיש באם א באות הראשונה ")
