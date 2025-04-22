import random
import string
from words import words  # This should be a list of valid words

def get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6  # number of tries

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left. Used letters:", " ".join(used_letters))
        
        # show the current word status
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(word_display))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please try again.")

    # Game over conditions
    if lives == 0:
        print(f"\nYou died. The word was {word}.")
    else:
        print(f"\nYay! You guessed the word {word} correctly!")

# Start the game
hangman()
