mylist=[]
newlist = []
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    x=int(input("Enter a element: "))
    mylist.append(x)

size = int(input("Enter the number of chunks: "))
for i in range(0, len(mylist), size):
    newlist.append(mylist[i:i+size])

print(f"The chunked list:  {newlist}")