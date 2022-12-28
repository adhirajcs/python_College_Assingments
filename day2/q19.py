mylist=[]
n=int(input("Enter the length of the list: "))
for i in range(0,n):
    x=int(input("Enter the element: "))
    mylist.append(x)
my_result = []
for i in mylist:
   val = 0
   for digit in str(i):
      val = val + int(digit)
   my_result.append(val)
print ("The result after adding the digits of the list elements: " )
print(my_result)