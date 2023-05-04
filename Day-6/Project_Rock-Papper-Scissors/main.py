# Welcome to Rock, Paper Scissors
import random

# ASCII art for Roc, Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Choices
options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

# Error handling for choice
if player_choice >= 3 or player_choice < 0:
    print("You have typed an invalid number. Disqualified!")
else:
    print(options[player_choice])
    print("Computer chose:")
    print(options[computer_choice])

    # Game logic
    if player_choice == computer_choice:
        print("You Draw!")
    elif player_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You Win")
    elif player_choice > computer_choice:
        print("You win!")
    elif player_choice < computer_choice:
        print("You Lose!")
