# Packages & Modules
import random
import my_module

# Generate a Random Number
random_integer = random.randint(1, 10)
print("--------------------------------------------------")
print(f"A random whole number: {random_integer}")
print("--------------------------------------------------")
print()

# Print PI from a custom module
print("--------------------------------------------------")
print(f"Printing Pi: {my_module.pi}")
print("--------------------------------------------------")
print()

# Print a random float
print("--------------------------------------------------")
random_float = random.random()
print(f"A random float: {random_float}")
print("--------------------------------------------------")
print()

# Print a random float with set range
print("--------------------------------------------------")
random_float_custom = random.uniform(0.0, 5.0)
print(f"A random float between 0 & 5: {random_float_custom}")
print("--------------------------------------------------")
print()

# Love calculator using random numbers
print("--------------------------------------------------")
love_score = random.randint(0, 100)
print(f"Your Love score is: {love_score}")
print("--------------------------------------------------")


