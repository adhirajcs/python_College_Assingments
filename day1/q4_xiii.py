""" 4. Write scripts to print each of the following output pattern.
The number of rows to be printed is to be 
accepted as user input. """
# Pattern xiii


row = int(input("Enter the number of rows: "))
n=(row-1)//2
for i in range(row):
    for j in range(row):
        if (i+j>=n and i<=n and j<=n) or (i>=n and j>=n and i+j<=3*n) :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()