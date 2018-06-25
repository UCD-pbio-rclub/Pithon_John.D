### Needed module for time saving
import string

### Problem 3 with a word
def word_palindrome(user_input):
    user_input = str(user_input)
    length = len(user_input)
    for character in range(length//2):
        if user_input[character] != user_input[-character-1]:
           print(user_input, "is not a palindrome")
           break
    else:
         print(user_input, "is a palindrome")
    return

### Problem 3 with a sentence ignore punctuation
def sentence_palindrome(user_input):
    query = "".join(str(user_input).lower().split())
    query = query.translate(str.maketrans('','',string.punctuation))
    length = len(query)
    for character in range(length//2):
        if query[character] != query[-character-1]:
           print(user_input, "is not a palindrome")
           break
    else:
         print(user_input, "is a palindrome")
    return

### Problem 3 with a sentence ignore punctuation and interactive
def interactive_palindrome():
    user_input = input("Enter a potential palindome:\n")
    query = "".join(user_input.lower().split())
    query = query.translate(str.maketrans('','',string.punctuation))
    length = len(query)
    for character in range(length//2):
        if query[character] != query[-character-1]:
           print(user_input, "is not a palindrome")
           break
    else:
         print(user_input, "is a palindrome")
    return

### Problem 3 with a sentence ignore punctuation and more interactive
def interactive_palindrome2():
    while True:
        user_input = input("Enter a potential palindome:\n")
        query = "".join(user_input.lower().split())
        query = query.translate(str.maketrans('','',string.punctuation))
        length = len(query)
        for character in range(length//2):
            if query[character] != query[-character-1]:
               print(user_input, "is not a palindrome")
               break
        else:
            print(user_input, "is a palindrome")
        repeat = input('Try another palindrome? [Y/n]: ').lower()
        repeat = repeat or 'y'
        if repeat == "n":
            print("Exiting program now")
            return
        


