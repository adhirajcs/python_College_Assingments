phrase = input("Enter words as input and seperate them by a comma only: ")
phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))