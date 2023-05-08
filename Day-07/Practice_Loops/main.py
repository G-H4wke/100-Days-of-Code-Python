# Create a list of fruits
fruits = ["Apple", "Peach", "Pear"]
desserts = ["Pie", "Cake", "Jelly"]

# Loop through the list
for fruit in fruits:
    print(fruit + " Options:")
    print("------------------------------")
    for dessert in desserts:
        print(fruit + " " + dessert)
    print()
