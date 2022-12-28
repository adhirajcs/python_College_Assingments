str = input("Enter the string :")
def palindrome(str):
    str = str.lower().replace(' ', '')
    return str == str[::-1]
if(palindrome(str)):
    print(f"{str} is Palindrome")
else:
    print(f"{str} is not Palindrome")