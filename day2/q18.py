mylist = []
for i in range(300,351):
    string = str(i)
    if (int(string[1])%2==0) and (int(string[2])%2==0):
        mylist.append(string)
print(','.join(mylist))