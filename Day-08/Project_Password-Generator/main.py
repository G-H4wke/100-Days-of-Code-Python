# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Password logic
character_choices = []

# Iterate through letters and choose x at random
for letter in range(0, nr_letters):
    character_choices.append(random.choice(letters))

# Iterate through symbols and choose x at random
for symbol in range(0, nr_symbols):
    character_choices.append(random.choice(symbols))

# Iterate through numbers and choose x at random
for number in range(0, nr_numbers):
    character_choices.append(random.choice(numbers))

# Randomise the Character Choices list into a new list
random_password_list = random.sample(character_choices, len(character_choices))

# Create an ordered password
ordered_password = ""
for item in character_choices:
    ordered_password += item

# Create a random password
random_password = ""
for character in random_password_list:
    random_password += character

# Print ordered and random passwords
print(f"Your ordered password is: {ordered_password}")
print(f"Your random password is: {random_password}")

