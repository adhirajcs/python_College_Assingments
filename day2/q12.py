mylist = []
n = int(input("Enter the number of values: "))
for i in range(0,n):
    value = input("Enter the value: ")
    mylist.append(value)
print("The original list: " + str(mylist))
startWithM = "M"
r = []
for s in mylist:
	temp = s.split()
	for element in temp:
		if element[0].lower() == startWithM.lower():
			r.append(element)
print("The Extracted element: " + str(r))