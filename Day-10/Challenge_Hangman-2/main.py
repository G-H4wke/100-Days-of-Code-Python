# Step 2
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Show an underscore per letter in chosen_word
display = []

for _ in chosen_word:
    display.append('_')
print(display)

# Ask user to guess the letter
guess = input("Guess a letter: ").lower()

# Loop through the chosen word and add the correct letter to display
for position in range(word_length):
    letter = chosen_word[position]
    if guess == letter:
        display[position] = letter

# Print current guess
print(display)
