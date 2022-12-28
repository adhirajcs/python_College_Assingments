n=int(input("Enter the range: "))
mylist=[]
for i in range(0,n):
    val=int(input("Enter the value: "))
    mylist.append(val)
print(f"{mylist} is the OG list")
size=len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print(f"{mylist} is the list after exchanging")
