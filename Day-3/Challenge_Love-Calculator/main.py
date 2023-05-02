# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line
lower_name1 = name1.lower()
lower_name2 = name2.lower()

combined_names = lower_name1 + lower_name2

# True check
t_score = combined_names.count("t")
r_score = combined_names.count("r")
u_score = combined_names.count("u")
e1_score = combined_names.count("e")

true_final_total = t_score + r_score + u_score + e1_score

# Love check
l_score = lower_name1.count("l")
o_score = lower_name1.count("o")
v_score = lower_name1.count("v")
e2_score = lower_name1.count("e")

love_final_total = l_score + o_score + v_score + e2_score

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
