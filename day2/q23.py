def is_vowel(s):
    return (s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U' or s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u')
string = input("Enter a string to convert to Pig Latin: ")
index = - 1
i=0
while(i<len(string)):
    if(is_vowel(string[i])):
        index = i
        break
    i=i+1

if(index==-1):
    print("No vowels, so cannot convert into Pig Latin")
elif(index==0):
    pig_latin = string[index:] + string[0:index] + "hay"
    print(f"The Pig Latin of {string} is {pig_latin}")
else:
    pig_latin = string[index:] + string[0:index] + "ay"
    print(f"The Pig Latin of {string} is {pig_latin}")