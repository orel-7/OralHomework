sam=0
for i in range(10):
    a=int(input("ציון"))
    if 10<a<99:
        print("סכום הספרות",(a%10)+(a//100))
    sam=sam+a
print("סכום הציוניים",sam)
