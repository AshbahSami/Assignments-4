import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is {player_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    
    # Extension #1: Input validation
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either higher or lower: ").lower()
    
    correct = False
    
    # Milestone #3: Game logic
    if player_number > computer_number and guess == "higher":
        correct = True
    elif player_number < computer_number and guess == "lower":
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    print(f"Your score is now {score}\n")

# Extension #2: Final evaluation
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
