mylist = []
newlist = [[]]
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    x=int(input("Enter a element: "))
    mylist.append(x)
for i in range(len(mylist)+1):
    for j in range(i):
        newlist.append(mylist[j:i])
print(newlist)
