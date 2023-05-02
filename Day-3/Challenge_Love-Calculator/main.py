# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line
lower_name1 = name1.lower()
lower_name2 = name2.lower()

# True check
name1_t = lower_name1.count("t")
name1_r = lower_name1.count("r")
name1_u = lower_name1.count("u")
name1_e1 = lower_name1.count("e")

name2_t = lower_name2.count("t")
name2_r = lower_name2.count("r")
name2_u = lower_name2.count("u")
name2_e1 = lower_name2.count("e")

# Love check
name1_l = lower_name1.count("l")
name1_o = lower_name1.count("o")
name1_v = lower_name1.count("v")
name1_e2 = lower_name1.count("e")

name2_l = lower_name2.count("l")
name2_o = lower_name2.count("o")
name2_v = lower_name2.count("v")
name2_e2 = lower_name2.count("e")

# True total Value
name1_true_total = name1_t + name1_r + name1_u + name1_e1
name2_true_total = name2_t + name2_r + name2_u + name2_e1
true_final_total = name1_true_total + name2_true_total

# Love Value total
name1_love_total = name1_l + name1_o + name1_v + name1_e2
name2_love_total = name2_l + name2_o + name2_v + name2_e2
love_final_total = name1_love_total + name2_love_total

# Love Score
true_love_combined = str(true_final_total) + str(love_final_total)
love_score = int(true_love_combined)

# Display Result
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
