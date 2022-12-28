mylist=[]
newlist = []
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    x=int(input("Enter a element: "))
    mylist.append(x)
final_list = [[mylist[i], mylist[i + 1]] for i in range(len(mylist) - 1)]
print("The Consecutive elements of the list are: ")
print(final_list)