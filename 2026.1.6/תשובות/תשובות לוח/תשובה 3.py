trip_price=int(input("מחיר טעיול"))
total_savings=0
while total_savings<trip_price:
    monthlyt=float(input("כמה כסף שושנה חסכה החודש? "))
    total_savings+=monthlyt
    print("עד כה נחסכו",total_savings)

print("חסכת מספיק כסף לטיול")
