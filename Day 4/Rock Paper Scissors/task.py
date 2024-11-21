import random

rock = '''
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

playerNumber = int(input("Type your choice: 1 for rock, 2 for paper, or 3 for scissors: \n"))
computerNumber = random.randint(1,3)

if playerNumber == 1:
    print("Player chose:" + rock)
elif playerNumber == 2:
    print("Player chose:" + paper)
else: print("Player chose:" + scissors)

if computerNumber == 1:
    print("Computer chose:" + rock)
elif computerNumber == 2:
    print("Computer chose:" + paper)
else: print("Computer chose:" + scissors)

if playerNumber == 1 and computerNumber == 3:
    print("You win!")
elif playerNumber == 2 and computerNumber == 1:
    print("You win!")
elif playerNumber == 3 and computerNumber == 2:
    print("You win!")
elif computerNumber == 1 and playerNumber == 3:
    print("You lose!")
elif computerNumber == 2 and playerNumber == 1:
    print("You lose!!")
elif computerNumber == 3 and playerNumber == 2:
    print("You lose!")
else: print("It's a draw.  Try again!")