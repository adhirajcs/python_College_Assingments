""" 2. Write a script that reads three floating point numbers, and does the following:  
i) It prints the smallest and largest among the three.
ii) It prints the average of the three numbers up to 2 decimal places. """


n1 = 10.23
n2 = 14.43
n3 = 12.56

if(n1<n2) and (n1<n3):
    smallest=n1
elif(n2<n1) and (n2<n3):
    smallest=n2
else:
    smallest=n3
print("The smallest number is ", smallest)
    
if(n1>n2) and (n1>n3):
    largest=n1
elif(n2>n1) and (n2>n3):
    largest=n2
else:
    largest=n3
print("The largest number is ", largest)

avg=(n1+n2+n3)/3
txt = "Average = {:.2f}"
print(txt.format(avg))