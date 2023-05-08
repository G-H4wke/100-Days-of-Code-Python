# Global
ticket_price = 0

# Welcome them to the roller coaster
print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

# Determine if they are able to ride the roller coaster
if height >= 120:
    print("You can ride the Roller Coaster!\n")

    age = int(input("What is your age? "))

    # Determine the ticket price
    if age < 12:
        ticket_price = 5
        print("Child Tickets are £5\n")
    elif age <= 18:
        ticket_price = 7
        print("Youth Tickets are £7\n")
    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ticket on us!\n")
    else:
        ticket_price = 12
        print("Adult Tickets are £12\n")

    # Check if they want a photo
    wants_photo = input("Do you want a photo taken? Y or N. ")

    # Final Ticket Price
    if wants_photo == "Y":
        ticket_price += 3

    # Display price to the user
    print(f"Your ticket price is £{ticket_price}")
else:
    print("Sorry, you need to be taller before you can ride.")
