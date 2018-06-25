### Problem 1
import random
from nltk.corpus import words as word_list

words = word_list.words()

def play_hangman():
    global lives_remaining
    global guessed_letters
    lives_remaining = 6
    guessed_letters = set()
    word = random.choice(words).lower()
    while True:
        gallows(lives_remaining)
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            gallows(0)
            print('You are Hung!')
            print('The word was: ' + word)
            break

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or the word:\n').lower()
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '-'
    print(display_word)

def process_guess(guess, word):
    if guess in guessed_letters:
        print('Guess has already been entered')
        print('Past guesses: ', guessed_letters)
        return False
    elif len(guess) == len(word):
        return word_guess(guess, word)
    elif len(guess) == 1:
        return letter_guess(guess, word)
    else:
        print('Guess is not a single letter or the length of the secret word')
        return False

def word_guess(guess, word):
    global lives_remaining
    global guessed_letters
    if guess == word:
        return True
    else:
        lives_remaining -= 1
        guessed_letters.add(guess)
        return False

def letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if guess not in word:
        lives_remaining -= 1
    guessed_letters.add(guess)
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def gallows(lives_remaining):
    print("_____________   ")
    print("|           |   ")
    if lives_remaining == 6:
        print("|")
    else:
        print("|           0   ")
    if lives_remaining == 5:
        print("|")
    else:
        if lives_remaining == 4:
            print("|           |   ")
        if lives_remaining == 3:
            print("|          /|   ")
        if lives_remaining <= 2:
            print("|          /|\\ ")
    if lives_remaining >= 2:
        print("|")
    else:
        if lives_remaining == 1:
            print("|          /    ")
        else:
            print("|          / \\ ")
            print("|   You Dead")
    print("|")
    return
    
