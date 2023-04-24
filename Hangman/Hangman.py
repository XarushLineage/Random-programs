import random
import urllib.request

# List of possible words to guess
# Retrieve the word list from the webpage
url = "https://raw.githubusercontent.com/XarushLineage/Random-programs/main/Hangman/wordlist.txt"
response = urllib.request.urlopen(url)
long_txt = response.read().decode()
word_list = long_txt.splitlines()

# Select a random word from the list
word = random.choice(word_list)

# Set up the game
guesses = []
maxfails = 6
fails = 0

# Greet the user.
print("You are playing Hangman!")

# Loop until the player has won or lost
while fails < maxfails:
    # Print the letters already used up
    print("Used letters:", ", ".join(guesses))

    # Print the current state of the word
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    # Ask the player for a guess
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guesses:
            print("You already guessed that letter. Please guess a different letter.")
        else:
            break

    # Check if the guess is in the word
    if guess in word:
        guesses.append(guess)
        print("Correct!")
    else:
        fails += 1
        guesses.append(guess)
        print("Wrong guess. You have", maxfails - fails, "tries left.")

    # Check if the player has won
    if set(word) == set(guesses):
        print("Congratulations, you won!")
        break

# Check if the player has lost
if fails == maxfails:
    print("You lost. The word was", word)
