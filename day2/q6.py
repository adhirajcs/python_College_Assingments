def duplChar(input):
	a=[]
	for i in input:
		if i not in a and input.count(i)>1:
			a.append(i)
	return " ".join(a)
inp = input("Enter the string:")
b = duplChar(inp)
if(b==""):
	print("There are no duplicate strings")
else:
	print(f"{b} are the duplicate strings")