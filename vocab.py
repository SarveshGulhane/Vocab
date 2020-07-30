import re
import string
from spellchecker import SpellChecker
import tkinter

dictionary = open('words.txt', 'r').read().split() # open text file
words = list(dictionary)  # create list of words
letters = list(string.ascii_lowercase)  # create list of alphabets
spell = SpellChecker()

# if user want list of words starts with any letter
def ListofWords():
    while True:
        letterInput = input("\nEnter few starting letters :")
        if letterInput != "/":
            tempList = []
            # used regular expresions to find words starting with given input
            for word in words:
                if re.findall('^' + str(letterInput), word) != []:
                    tempList.append(word)
            print("Words:\n", tempList)
        else:
            break

# if user want spell check
def SpellCheck():
    while True:
        wordInput = input("\nEnter a word: ")
        if wordInput != "/":
            # if input word is in list of words
            if wordInput in words:
                print("Correct spelling!!")
            else:
                # if word is not in list of words, then use SpellChecker library
                print("Incorrect spelling..")
                print('Do you mean: ', spell.correction(wordInput))
                print('Suggestions: ', spell.candidates(wordInput))
        else:
            break

while True:
    choice = int(input('''
    Welcome!
    1. List of words
    2. Spell check
    3. Exit
    What you want to do: '''))

    if choice == 1:
        ListofWords()
    if choice == 2:
        SpellCheck()
    if choice == 3:
        break
    if choice > 3:
        print("Enter valid option\n")
        continue
