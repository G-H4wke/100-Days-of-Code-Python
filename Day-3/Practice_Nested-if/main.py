# Welcome them to the roller coaster
print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

# Determine if they are able to ride the roller coaster
if height >= 120:
    print("You can ride the Roller Coaster!")

    age = int(input("What is your age? "))

    # Determine the ticket price
    if age < 12:
        print("Please pay £5")
    elif age <= 18:
        print("Please pay £7")
    else:
        print("Please pay £12")
else:
    print("Sorry, you need to be taller before you can ride.")