import re
import string
from spellchecker import SpellChecker
import tkinter

dictionary = open('words.txt', 'r').read().split() # open text file
words = list(dictionary)  # create list of words
letters = list(string.ascii_lowercase)  # create list of alphabets
spell = SpellChecker()

# if user want list of words starts with any letter
def list_of_words():
    while True:
        letter_input = input("\nEnter few starting letters :")
        if letter_input != "/":
            temp_list = []
            # used regular expresions to find words starting with given input
            for word in words:
                if re.findall('^' + str(letter_input), word) != []:
                    temp_list.append(word)
            print("Words:\n", temp_list)
        else:
            break

# if user want spell check
def spell_check():
    while True:
        word_input = input("\nEnter a word: ")
        if word_input != "/":
            # if input word is in list of words
            if word_input in words:
                print("Correct spelling!!")
            else:
                # if word is not in list of words, then use SpellChecker library
                print("Incorrect spelling..")
                print('Do you mean: ', spell.correction(word_input))
                print('Suggestions: ', spell.candidates(word_input))
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
        list_of_words()
    if choice == 2:
        spell_check()
    if choice == 3:
        break
    if choice > 3:
        print("Enter valid option\n")
        continue
