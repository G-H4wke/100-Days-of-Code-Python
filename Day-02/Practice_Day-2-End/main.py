# Converting Int to Str to display to the user
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name is " + new_num_char + " characters.\n")

# Checking data types with type()
print("-------------")
print("num_char is of type:")
print(type(num_char))
print("new_num_char is of type:")
print(type(new_num_char))
print("-------------")
print()

# Adding two number data types together by converting a string
print("-------------")
print(70 + float("100.5"))
print("-------------")
print()

# Concatenating a string after converting two numbers
print("-------------")
print(str(70) + str(100))
print("-------------")
