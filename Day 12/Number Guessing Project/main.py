import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ").lower()

NUMBER = random.randint(1, 100)
guess = 0

attempts = 0

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while guess != NUMBER and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess > NUMBER:
        print("Too High.\nGuess Again")
    elif guess < NUMBER:
        print("Too Low.\nGuess Again")
    else:
        print(f"You got it! The answer was {NUMBER}.")
print("You Ran out of guesses.  You lose, sucka!")