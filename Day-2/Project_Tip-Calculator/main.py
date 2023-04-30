# The goal is to create a tip calculator that calculates the total amount with a tip and split the bill.

# Welcome Message
print("Welcome to the Tip Calculator!")

# Gather the required information
total_bill = float(input("What was the total bill? £"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

# Calculate the total bill per person
total_tip = 1 + percentage_tip / 100
total_with_tip = total_bill * total_tip
total_per_person = total_with_tip / number_of_people
final_amount = "{:.2f}".format(total_per_person)

# Display result
print(f"Each person should pay: £{final_amount}")
