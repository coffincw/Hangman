import random
import sys
import os

word_library = ["abyss", "habit", "welcome", "meeting", "trial", "wildfire", "quarter", "community"]

print("Welcome to Hangman")
word = word_library[random.randrange(0, 8)]
slots = len(word)
print("The word is %d letters long " %
      (slots))

print("What is your letter guess?")
guess = sys.stdin.readline()
if word.__contains__(guess):
    print("Good guess, %s was in the word %")


