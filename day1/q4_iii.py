""" 4. Write scripts to print each of the following output pattern.
The number of rows to be printed is to be 
accepted as user input. """
# Pattern iii


row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(row):
        if i<=j:
            print("*", end=" ")
    print()