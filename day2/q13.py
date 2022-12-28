mylist=[]
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    a=int(input("Enter a element: "))
    mylist.append(a)
N = int(input("Enter the value of N: "))
final_list=[]
for i in range(0, N):
    max1=0
    for j in range(len(mylist)):
        if mylist[j]>max1:
            max1=mylist[j]    
    mylist.remove(max1)
    final_list.append(max1)  
print(final_list)    
