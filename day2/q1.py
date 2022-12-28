string = input("Enter the String: ")
number =int(input("Enter the number to rotate by: "))
Lf = string[0 : number]
Ls = string[number :]
Rf = string[0 : len(string) - number]
Rs = string[len(string) - number : ]
print ("Left Rotation : ", (Ls + Lf) )
print ("Right Rotation : ", (Rs + Rf))