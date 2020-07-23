# Quiz Lesson 6

<br>

## Quiz: Flying Circus Cast List

You're going to create a list of the actors who appeared in the television programme Monty Python's<br>Flying Circus.

Write a function called `create_cast_list` that takes a filename as input and returns a list of actors'<br>names. 
It will be run on the file [`flying_circus_cast.txt`](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/flying_circus_cast.txt)
(this information was collected from<br>imdb.com). 
Each line of that file consists of an actor's name, a comma, and then some (messy)<br>information about roles they played in the programme. 
You'll need to extract _only_ the name and add it<br>to a list. 
You might use the [`.split()` method](https://docs.python.org/3/library/stdtypes.html#str.split) to process each line.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/cast_list.py)

<br>

## Quiz: Password Generator

Write a function called `generate_password` that selects three random words from the list of words<br>`word_list` (present in the file [`words.txt`](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/words.txt))
and concatenates them into a single string.
Your function should not accept any arguments<br>and should reference the global variable `word_list` to build the password.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/password_generator.py)

## Quiz

**Question:** Create a function that opens the [`flowers.txt`](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/flowers.txt), 
reads every line in it, and saves it as a<br>dictionary. 
The main (separate) function should take user input (user's first name and last name) and<br>parse the user input to identify the first letter of the first name. 
It should then use it to print the flower<br>name with the same first letter (from dictionary created in the first function).

**Sample Output:**  

```
>>> Enter your First [space] Last name only: Bill Newman
>>> Unique flower name with the first letter: Bellflower
```

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_6/match_flower_name.py)
