names = ["Samuel", "Adi", "Roi", "Moshe", "Adi"]

names.append("Dana")

print(names.count("Adi"))

for name in names:
    if names.count(name) > 1:
        print(name)

for name in names:
    print(name)