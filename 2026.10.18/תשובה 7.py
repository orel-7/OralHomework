amount=int(input("Enter a price: "))

coins10 = amount//10
amount %= 10

coins5 = amount//5
amount %= 5

coins2 = amount//2
amount %= 2

coins1=amount

print(f"10₪ coins:",coins10)
print(f"5₪ coins:",coins5)
print(f"2₪ coins:",coins2)
print(f"1₪ coins:",coins1)