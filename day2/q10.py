str = input("Enter the Snake Case String: ")
x = str.split("_")
pascalStr=""
for i in x:
    pascalStr+=i.capitalize()
print(pascalStr)
camelStr=x[0]
for i in x[1:]:
    camelStr+=i.capitalize()
print(camelStr)