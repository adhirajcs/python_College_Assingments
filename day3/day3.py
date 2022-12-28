# -*- coding: utf-8 -*-
"""day3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDMrX7ZJLIZBySgcNilWmDTeD8zjGC-6
"""

#q1
my_list = [('Adnan', 25, "Programmer"), ("Swati", 27, 'DBA'), ('Anand', 26, "Tester")]

for a in my_list:
    name, age, occupation = a
    print(f"{name} is {age} years old and works as {occupation}.")

#q2
inp=int(input("Enter a 3 digit number: "))
result = ""
letters = [(4, "r"), (2, "w"), (1, "x")]

for i in [int(n) for n in str(inp)]:
        
        for x, l in letters:
            if i >= x:
                result += l
                i -= x
            else:
                result += "-"
print(f"The file permission is: {result}")

#q3
dict1 = {'a': 1, 'b': 2, 'c': 3}

my_list = [(k,v) for k,v in dict1.items()]
print(my_list)

#q4
my_tuple = (56,5,6,1,2)

x = set(my_tuple)
x = sorted(x)
temp = tuple(x)
k = 2
print(f"The maximum {k} elements: {temp[-k:]}")
print(f"The minimum {k} elements: {temp[:k]}")

#q5
my_list = [2, 5, 1, 4]
rs = [(i,i**2) for i in my_list]
print(rs)

#q6
dict1 = {1:[1,4,3,2],
         2:[5,6,7,8],
         3:[3,6,5,1]}

rs = list(set(sorted(element for value in dict1.values() for element in value)))
print(rs)

#q7
dict1 = {1: "Jan", 2: "Feb", 3: "Mar"}
l=[]
for i in dict1:
    l.append(i)
for i in dict1:
    l.append(dict1[i])
print(l)

#q8
dict1 = {2:'Jan', 1:'March', 4:'Oct',5:'July',3:'Dec'}

dict2={}
for i,j in sorted(dict1.items()):
    dict2[i]=j
print(dict2)

dict3={}
for i,j in sorted([(v,k) for k,v in dict1.items()]):
    dict3[j]=i
print(dict3)

#q9
s = "Python is great and java is also great "
print(s)
l = s.split()
k =[]
for i in l:
    if (s.count(i)>=1) and (i not in k):
        k.append(i)
print(" ".join(k))

#q10
st = ("This is a sentence.").lower()
print(st)
rs = {}

for i in st:
    if i .isalpha() and i not in rs:
        rs[i] = st.lower().count(i)
print(rs)

#q11
st = ("""Fear leads to anger; Anger leads to hatred; Hatred leads to conflict;
Conflict leads to suffering.""").lower()

specialChar =  ['~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
for i in specialChar:
    st = st.replace(i,' ')
x = st.split()
rs = {}

for i in x:
    if i in rs:
        rs[i] += 1
    else:
        rs[i] = 1
print(rs)

#q12
list1 = ["program.c", "stdio.cpp", "sample.cpp", "a.out", "math.cpp", "cpp.out"]
print([i.replace('.cpp','.h') for i in list1])

#q13
dict1 = {"gmail.com": ["paul.buchheit", "sanjeev.singh", "kevin.fox"], "yahoo.com": ["jerry.yang", "david.filo"], "hotmail.com": ["sabeer.bhatia"]}
list1 = []
for k,v in dict1.items():
    for v2 in v:
        st = f"{v2}@{k}"
        list1.append(st)
print(list1)

#q14
dict1 = {"local":["admin", "Ananya"],"public":["admin", "Zahir"], "administrator":["admin"] }
dict2={}
for i in dict1:
    for j in dict1[i]:
        if j not in dict2:
            dict2[j]=[i]
        else:
            dict2[j].append(i)
print(dict2)

#q15
groc = {"apples": 100.50,"bananas": 40, "oranges": 150, "bread": 12.50, "milk": 23.50, "eggs": 39}
sum = 0
for price in groc.values():
    sum = sum + price
groc["total"] = sum
print(groc)

#q16
dict1 = {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
totalMarks = sum(dict1["marks"])
dict1["total"] = totalMarks
print(dict1)

dict2 = {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
dict2["marks"].append(totalMarks)
print(dict2)

dict3 = {"roll": 5, "Name": "Ananya", "marks": [79, 88, 92]}
dict3["marks"] = totalMarks
print(dict3)