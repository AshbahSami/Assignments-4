import random

secret_number = random.randint(1, 99)
print("I am thinking of a number from 1 to 99.")

guess = int(input("Enter a guess: "))

while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    
    guess = int(input("Enter a guess: "))

print("You guessed correctly!")
