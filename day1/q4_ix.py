""" 4. Write scripts to print each of the following output pattern.
The number of rows to be printed is to be 
accepted as user input. """
# Pattern ix


row = int(input("Enter the number of rows: "))

for i in range(row):
    for j in range(row):
        if (i<=j and i+j>=row-1) or (i+j<=row-1 and i>=j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()