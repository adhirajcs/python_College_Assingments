mylist = []
inp = [x for x in input("Input comma separated sequence of strings: ").split(',')]
for i in inp:
    binary = int(i, 2)
    if not binary%3:
        mylist.append(i)

if(len(mylist)==0):
    print("No binary numbers that are given are divisible by 3!")
else:
    print(','.join(mylist))