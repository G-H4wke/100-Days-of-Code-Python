# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

# Write your code below this line
number_remainder = number % 2

if number_remainder > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
