import random

word_library = ["abyss", "habit", "welcome", "meeting", "trial", "wildfire", "quarter", "community"]


word = word_library[random.randrange(0, len(word_library))]
answer = list(word)

slots = len(word)
gameboard = []
for i in word:
    gameboard.append('_')

picks = []

def inputGuess(guess):
    while (len(guess) > 1 or len(guess) < 1):
        guess = input("What is your letter guess?")
        guess = guess.lower()
        if (len(guess) > 1):
            print("Please input one letter")
        elif len(guess) < 1:
            print("Please input a letter")
        else:
            return guess

class Hangman():
    rightletters = 0
    print("Welcome to Hangman")
    print(gameboard)
    wrongguesses = 10
    while (wrongguesses > 0):
        guess = ''

        print("The word is %d letters long " %
              (slots))
        guess = inputGuess(guess)

        times = 0
        iterate = 0
        for i in answer:
            iterate += 1
            if guess == i:
                times += 1
                rightletters += 1
                del gameboard[iterate - 1]
                gameboard.insert(iterate - 1, guess)

        if times > 0:
            print("Good guess, %s was in the word %d time(s)" %
                  (guess, times))

        picks.append(guess)

        if times < 1:
            wrongguesses -= 1
            print("Sorry, pick again! You have %d guesses left" % (wrongguesses))
        if rightletters == slots:
            print("Congratuations! You guessed the word '%s' correctly!" % (word))
            break
        else:
            print("Game board: %s" % (gameboard))
            print("You have guessed %s " % (picks))
            print("--------------------------------")




