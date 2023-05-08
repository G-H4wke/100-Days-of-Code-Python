# Begin the Treasure Hunt Adventure!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# The First Choice
print("You are in a forest. To the left you see the forest go deeper and too the right you see a faint light.")
first_choice = input("Do you go 'Left' or 'Right'?\n").lower()

if first_choice == "right":
    print("You ran towards the light...and fell straight off a cliff. Game Over!")
elif first_choice == "left":
    print("You go deeper into the forest and come to a crossing. You see a temple in the distance.")

    # The Second Choice
    second_choice = input("Do you 'wait' for a boat or 'swim' to the other side? \n").lower()

    if second_choice == "swim":
        print("As you swim across you feel a tingling sensation on your leg. You get a sudden cramp and the tide "
              "takes you to an opening...and straight off a clif. Game Over!")
    elif second_choice == "wait":
        print("Your patience paid off! A giant Turtle takes you to the temple and you see three doors.")

        # The Final Choice
        final_choice = input("Choose wisely. Do you choose the 'Red' door, the 'Blue' door or 'Green' door? \n").lower()

        if final_choice == "red":
            print("The door is locked. Game Over!")
        elif final_choice == "blue":
            print("You open the door to find a Chest full of Treasure! You won the game!")
        elif final_choice == "green":
            print("The door opens to a bright light. You walk through...and fall straight off a cliff. Game Over!")
