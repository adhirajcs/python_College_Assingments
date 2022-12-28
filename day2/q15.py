def sort(l):
    ascending = descending = True
    i = 0
    L = len(l)
    while (i < (L-1)) and (ascending or descending):
        if l[i] < l[i+1]:
            descending = False
        elif l[i] > l[i+1]:
            ascending = False
        if not (ascending or descending):
            break
        i += 1
    if ascending:
        return "The list is ascending!!!"
    elif descending:
        return "The list is descending!!!"
    else:
        return "The list is not sorted!!!"
mylist=[]
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    x=int(input("Enter a element: "))
    mylist.append(x)
print(f"{sort(mylist)}")