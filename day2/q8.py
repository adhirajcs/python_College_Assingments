def stringGreaterThan_k(valk, str):
	st = []
	text = str.split(" ")
	for i in text:
		if len(i) > valk:
			st.append(i)
	return st
str = input("Enter the String: ")
valk = int(input("Enter the length: "))
print(stringGreaterThan_k(valk, str))