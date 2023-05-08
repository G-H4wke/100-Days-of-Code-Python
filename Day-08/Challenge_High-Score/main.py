# Don't change the code below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

# Write your code below this row
current_highest_number = 0

# Loop through the list
for score in student_scores:
    # compare the current number with the previous number
    if score > current_highest_number:
        current_highest_number = score

# Store the high-score
high_score = current_highest_number

# Print out the highest number
print(f"The highest score in the class is: {high_score}")
