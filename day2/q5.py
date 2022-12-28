str = input("Enter your String: ")
splt = str.split()[::-1]
mylist = []
for i in splt:
    mylist.append(i)
print(" ".join(mylist))