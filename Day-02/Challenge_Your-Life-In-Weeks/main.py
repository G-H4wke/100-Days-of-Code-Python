# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

# Write your code below this line
max_age = 90
current_age = int(age)

total_months = max_age * 12
total_weeks = max_age * 52
total_days = max_age * 365

months_left = total_months - (current_age * 12)
weeks_left = total_weeks - (current_age * 52)
days_left = total_days - (current_age * 365)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
