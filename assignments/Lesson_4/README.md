# QUIZ LESSON 4

<br>

## Quiz: Which Prize

Write an `if` statement that lets a competitor know which of these prizes they won based on the<br>
number of points they scored, which is stored in the integer variable `points`.

**Points** | **Prize**
:--------: | :-------:
1 - 50     | wooden rabbit
51 - 150   | no prize
151 - 180  | wafer-thin mint
181 - 200  | penguin

All of the lower and upper bounds here are inclusive, and `points` can only take on positive integer<br>values up to 200.

In your `if` statement, assign the `prize` variable to store a prize name if one was won, 
and then use the truth value<br>of this variable to compose the `result` message.

- If `prize` is None, `result` should be set to `"Oh dear, no prize this time."`
- If `prize` contains a prize name, `result` should be set to<br>`"Congratulations! You won a {}!".format(prize)`. 
This will avoid having the multiple<br>result assignments for different prizes.

At the beginning of your code, set prize to None, as the default value.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/give_prize.py)

<br>

## Quiz: Guess My Number

You decide you want to play a game where you are hiding a number from someone. Store this number<br>in a variable called 'answer'. 
Another user provides a number called 'guess'. By comparing guess to<br>answer, you inform the user if their guess is too high or too low.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/guess_number.py)

<br>

## Quiz: Create Usernames

Write a `for` loop that iterates over the `names` list to create a `usernames` list. 
To create a username<br>for each name, make everything lowercase and replace spaces with underscores. 
Running your `for`<br>loop over the list:

`names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]`

should create the list:

`usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]`

**HINT:** Use the [`.replace()`](https://docs.python.org/3/library/stdtypes.html#str.replace) method to replace the spaces with underscores.
Check out how to use<br>this method in this [Stack Overflow answer](https://stackoverflow.com/a/12723785).

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/create_usernames.py)

<br>

## Quiz: Create an HTML List

Write some code, including a `for` loop, that iterates over a list of strings and creates a single string,<br>`html_str`, which is an HTML list. 
For example, if the list is<br>`items = ['first string', 'second string']`, printing `html_str` should output:

```
<ul>
<li>first string</li>
<li>second string</li>
</ul>

```

That is, the string's first line should be the opening tag `<ul>`. Following that is one line per element in<br>the source list, surrounded by `<li>` and `</li>` tags. 
The final line of the string should be the closing<br>tag `</ul>`.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/html_list.py)

<br>

## Quiz: Factorials with For Loops

Find the factorial of a number using a `for` loop.

A **factorial** of a whole number is that number multiplied by every whole number between itself and 1.<br> 
For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.

Example: If `number` is 6, your code should compute and print the `product`, 720.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/factorial.py)

<br>

## Quiz: Nearest Square

Write a `while` loop that finds the largest square number less than an integer `limit` and stores it in a<br>variable `nearest_square`. 
A square number is the product of an integer multiplied by itself, for<br>example 36 is a square number because it equals 6*6.

For example, if `limit` is 40, your code should set the `nearest_square` to 36.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/nearest_square.py)

<br>

## Quiz: Check for Prime Numbers

Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few<br>prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.  
1 X 6 = 6  
2 X 3 = 6  
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list<br>`check_prime` are prime numbers.

- If the numbers are prime, the code should print "[number] is a prime number."
- If the number is NOT a prime number, it should print "[number] is not a prime number", and a<br>factor of that number, other than 1 and the number itself: 
"[factor] is a factor of [number]".

**Example output:**

```
7 IS a prime number
26 is NOT a prime number, because 2 is a factor of 26
```

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/prime_numbers.py)

<br>

## Quiz: Transpose with Zip

Use `zip` to transpose `data` from a 4-by-3 matrix to a 3-by-4 matrix.<br>There's actually a cool trick for this!

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/transpose_matrix.py)

<br>

## Quiz: Filter Names by Scores

Use a list comprehension to create a list of names `passed` that only include those that scored at least<br>65.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/filter_names.py)

<br>

## Quiz

### Introduction

The following questions are based on data on Oscar Award Nominations for Best Director between the<br>years 1931 to 2010. 
To start you off, we've provided a dictionary called "nominated" with the year (as<br>key) and list of directors who were nominated in that year (as value). 
We've provided you with a<br>different dictionary called "winners" with the year (as key) and list of directors who won the award in<br>that year (as value).

### Practice Questions

#### Question 1.

**A. Create a dictionary that includes the count of Oscar nominations for each director in the<br>nominations list.**

**B. Provide a dictionary with the count of Oscar wins for each director in the winners list.**

#### Question 2:

**Provide a list with the name(s) of the director(s) with the most Oscar wins. 
We are asking for a list<br>because there could be more than 1 director tied for the most Oscar wins.**

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_4/oscar_award.py)
