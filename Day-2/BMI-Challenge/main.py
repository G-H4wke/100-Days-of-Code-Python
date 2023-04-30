# Challenge: Display Users BMI
# ----------------------------

# Do not change this
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Enter your code below
# ---------------------
num_height = float(height)
num_weight = float(weight)

bmi = int(num_weight / (num_height ** 2))

print(bmi)
