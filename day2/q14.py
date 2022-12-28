name_string=input("Enter a full name: ")
x = name_string.split()
if(len(x)==1):
    print(name_string)
else:
    string=""
    for a in x[:(len(x)-1)]:
        string += f"{a[0]}. "
    string += x[len(x)-1]
    print(string)
