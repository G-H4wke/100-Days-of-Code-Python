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

print(options[player_choice])
print("Computer chose:")
print(options[computer_choice])

# Game logic

if player_choice == 0:
    if computer_choice == 2:
        print("You Win!")
    elif computer_choice == 1:
        print("You Lose!")
    else:
        print("You Draw!")
elif player_choice == 1:
    if computer_choice == 0:
        print("You Win!")
    elif computer_choice == 2:
        print("You Lose!")
    else:
        print("You Draw!")
elif player_choice == 2:
    if computer_choice == 1:
        print("You Win!")
    elif computer_choice == 0:
        print("You Lose!")
    else:
        print("You Draw!")
