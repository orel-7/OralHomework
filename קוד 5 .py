A=0
B=0
for C in range(10):
    D = int(input("הכנס מספר סליל "))
    if 70 <= D <= 90:
        A += 1
    E = sum(int(x) for x in str(D))
    if E % 3 == 0:
        B += 1
print("מספר הסלילים בין 70 ל-90 ", A)
print("מספר הסלילים שסכום ספרותיהם מתחלק ב-3 ", B)
