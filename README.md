# 100-Days-of-Code-Python
---
I decided to challenge myself and commit to learning python properly by attempting the 100 days of code challenge.

Now I can be a bit impatient so there may be one or two days committed in a day! However, in the spirit of 100 days of code, I will do one a day and with each day, a project to tie all the concepts together!

## HAPPY CODING!!

---

## Day 1 - Band Name Generator
So for this day we looked at the print function. One of the most common functions you will
find used in the early days of your python journey.

Within this day we also looked at the input function. This function allows you to
take a string of text inputted by the user, return the resulting value and essential
"replace" the input function.

### What do you mean replace?
Well the input function will work alot like print where you can provide a string of
text to display to the user, such as "Hello, what is your name?". As soon as that statement
has been printed, you will see the cursor waiting for input. Once the user has entered
the string they want such as "Gabriel", that value is replacing the original printed text

pretty neat right?

### What can I do with it?

Well since it returns a value, rather than it just replace what was in the input,
 we can store that in a variable such as:
```python
name = input("Hello, What is your name? ")
```

Now we have a value, and we have stored it in a variable, we can use it wherever we like!

This was the basis of the Band Name Generator by storing inputs and coming up with a cool
band name.

---

## Day 2 - Tip calculator

So today we looked at how to manipulate data types along with a neat way to display a
string without having to manually use methods like int() or str() by using f-string.

By taking all of this information, and what we learned from the previous day, we were
tasked with creating a tip calculator. This project required you to input the total bill
amount, what percentage tip you would like to give, and how many people to split the bill between.

### Sounds pretty simple...right?
Well yes, it wasn't a huge jump from the previous day as it focused on similar topics
that we already covered. However, we also learned about other data types such as floats, doubles
and booleans.

This all came together when we used f-string or string interpolation to display our variables
in a print statement without needing to convert the data type. This was really useful

### Interesting tip!
Forgive the pun, but we found something very useful during the project called the format
method.

With this method you can choose how you want the result of your variable to be formatted.
For example if we want to display a variable with two decimal places after the result of a
division you can use:

```python
variable_name = "{:.2f}".format(25.3625)
```

In this case if we printed that variable it will show as 25.36! Neat.
