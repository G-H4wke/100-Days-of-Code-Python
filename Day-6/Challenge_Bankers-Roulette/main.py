# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

# Write your code below this line
max_item_range = len(names) - 1

random_choice = random.randint(0, max_item_range)
final_choice = names[random_choice]

print(f"{final_choice} is going to buy the meal today!")
