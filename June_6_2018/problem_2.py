### Problem 2
import string
def sentence_swap(sentence):
    sentence = sentence.lower()
    if sentence[-1] in string.punctuation:
        end = sentence[-1]
        sentence = sentence[:-1]
    else:
        end = ""
    split_sentence = sentence.split()
    split_sentence.reverse()
    new_sentence = " ".join(split_sentence) + end
    new_sentence = new_sentence.capitalize()
    return new_sentence

### Problem 2 Interactive
import string
def sentence_swap_interactive():
    sentence = input("Please enter a sentence to reverse:\n").lower()
    if sentence[-1] in string.punctuation:
        end = sentence[-1]
        sentence = sentence[:-1]
    else:
        end = ""
    split_sentence = sentence.split()
    split_sentence.reverse()
    new_sentence = " ".join(split_sentence) + end
    new_sentence = new_sentence.capitalize()
    return new_sentence
