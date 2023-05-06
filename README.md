# 100-Days-of-Code-Python
---
I decided to challenge myself and commit to learning python properly by attempting the 100 days of code challenge.

Now I can be a bit impatient, so there may be one or two days committed in a day!
However, in the spirit of 100 days of code, I will do one a day and with each day,
a project to tie all the concepts together!

## HAPPY CODING!!

---

## Day 1—Band Name Generator
So for this day we looked at the print function. One of the most common functions you will
find used in the early days of your python journey.

Within this day we also looked at the input function. This function allows you to
take a string of text inputted by the user, return the resulting value and essential
"replace" the input function.

### What do you mean "replace"?
Well, the input function will work alot like print where you can provide a string of
text to display to the user, such as "Hello, what is your name?". As soon as that statement
has been printed, you will see the cursor waiting for input. Once the user has entered
the string they want such as "Gabriel", that value is replacing the original printed text

pretty neat, right?

### What can I do with it?

Well, since it returns a value, rather than it just replaces what was in the input,
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
Well, yes, it wasn't a huge jump from the previous day as it focused on similar topics
that we already covered. However, we also learned about other data types such as floats, doubles
and booleans.

This all came together when we used f-string or string interpolation to display our variables
in a print statement without needing to convert the data type. This was really useful

### Interesting tip!
Forgive the pun, but we found something very useful during the project called the format
method.

With this method, you can choose how you want the result of your variable to be formatted.
For example, if we want to display a variable with two decimal places after the result of a
 division, you can use:

```python
variable_name = "{:.2f}".format(25.3625)
```

In this case, if we printed that variable, it will show as 25.36! Neat.

---

## Day 3—Treasure Hunt

Today was fun indeed. So with the practice, there was a heavy focus on Conditional
Statements, Logical Operators, Code Blocks and Scope within python. These are core
foundation concepts across all languages, and understanding this will help you with
any challenge in the future.

The Project for the day was a "Choose your own adventure" game, just like Zork!
By understanding control flow and the previous concepts we learnt, this text based game
came to life!

### So a quick day then?

Quite the opposite.
Day 3 introduces some more challenges,
and as time goes on, there will be more challenges than concepts practices to learn to really get the brain working!

We updated our BMI-Calculator using a control flow and string interpolation to a greater
degree. We created a Leap Year calendar, Pizza calculator (improving on our Tip calculator
 on the previous day) and a love calculator (I got 97 ;D ).

### Sounds like a lot of fun!
There were some great challenges on this day, and with all of this knowledge, we created
a Treasure Hunt text based adventure.

Whilst the concepts are relatively simple, this can really be improved upon and I would love
to come back to this at a later date and make this into a full-blown game!

---

## Day 4 - Practice!
Day 4 was a short day for Python as work had some intense SQL query to debug and figure out.

However, we still managed to get a small change in for Head and tails using a new module called
random.

### What now?
A Module!
Python has a lot of modules and packages, and this is one of the reasons it is such a
well-loved language.

We learnt about importing modules and using a powerful module called 'Random'. The challenge allowed
us to create a random float or int and use this to make a simple heads or tails game.

That combined with uploading the Rest of Day 3's challenges made for quite an interesting day

---

## Day 5 - List, List, List!

Another day, another practice!.
This practice is all building up to complete a rock, paper,
scissors project using the information learnt in Day 4 and 5. The idea was to get it done in one day
however, even if you are unable to, you must try your best to get some practice in each day!

So for my Day 5, we learnt about a new concept: lists and offsets and what this all means.

### So, a To-Do list?
Yes!

It is the concept of taking a single variable that has a list of data, like a string or an integer.
These "Data Structures" are paramount to every day in the programming world and is a concept we should
all learn as programmers.

This combined with some My SQL made up for the practice today. Day 6 will prove to be interesting!

---

## Day 6 - Rock, Paper, Scissors!

Day 6 culminated in our Rock, Paper, Scissors project, which took all the skills from the
previous challenges and practice sessions into one. 

We had lists, nested loops, offset and the good old print statement.

We also took random to another level by completing a challenge called Banker's Roulette

### Bankers what now?
Banker's roulette is where people would sit around a table and grab a meal, for instance.
Once the meal is completed, all the members of the party would put their bank cards 
in a bowl.

One card will be picked out at random to pay for the entire meal! This challenge was to take a list
of names, and randomly pick out a name from that list (all without using the choice() method).

### What did you learn?
The most important thing I learnt within these sessions is that there is more than one way to complete a task,
and it is okay to write something, and refactor it later.

To this day, in my coding career, I've still liked to complete everything perfect first time.

It is getting a lot easier now to "relax" and simply iterate over my code bit by bit.

A little day by day is all you really need!

---

## Day 7 — Over and Over

Today was a small amount of practice that only consisted of learning about loops.

Loops are a fundamental part of programming and are seen everywhere.
Whilst today was a light touch in my practice, as mentioned yesterday, a little is better every day.

### Committing every day can be a challenge.

It can, but what is important is if you keep learning, however, little you can that day, each and every
day thereafter will be easier to grab various concepts, and you can learn more in a short space of time.

With that, I also added another challenge to day 7 that I finished off to round off a successful day.

---

## Day 8—Python gone wild!

Day was the day the buzz was caught.
It was one challenge after another, and it just kept getting better!

One of the coolest parts of today's challenges was looking at the pre-built python functions
and then trying to implement a solution without using them like max(), sum() or len()

### So you had a range of challenges

Speaking of range, that was something newly introduced.
Up until this point, we have been using it for loops and lists to iterate over.
Range allowed us to specify two values like (0, 101) and loop through each number until 100.

### This sounds useful
Indeed, it is!

We used the combined ability for loops, range and if statements to complete the classic
FizzBuzz challenge.

This is a common programming interview question.
Whilst the logic is relatively easy, the goal of these questions is to usually test the way the interview thinks,
their thought process on solving the problem.

There are numerous was to solve the problem besides the quickest or most verbose.
I would like to see how many ways in python this can be completed!

### But that's not all
The project Password Generator was a lot of fun to complete. 

We were able to use all the knowledge from before (loops, list appends. range) to create
a randomly generated password of any length, chosen by the user.

Part-way through the project, we had to figure out how to randomise a list.
This came from using random.sample()

Sample is a great method where you can provide a population sequence and a length, 
and the method will return a randomised sequence without replacing the original list.

We could have used random.shuffle() however, I wanted to show what the password would
look like ordered and randomised (also, there is a warning about performance with large
sequences, and I wanted to avoid that for future-proofing)