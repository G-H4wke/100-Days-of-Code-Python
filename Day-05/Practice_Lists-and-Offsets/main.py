# Create a list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

# Print an item from the list - Index 0 based list
# Think of the list like an "offset" the first item is at the beginning, so it has no offset
print("------------------------------")
print(states_of_america[0])
print(states_of_america[1])
print("------------------------------")
print()

# Negative offset
# -1 is the last item in the list
print("------------------------------")
print(states_of_america[-1])
print("------------------------------")
print()

# Alter a list item
states_of_america[1] = "PencilVania"
print(states_of_america)
print()

# Append an item to the list
states_of_america.append("Massachusetts")
print(states_of_america)
print()

# Append multiple items to a list
states_of_america.extend(["Maryland", "South Carolina"])
print(states_of_america)
print()
