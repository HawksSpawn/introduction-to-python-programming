# Quiz Lesson 5

<br>

## Quiz: `readable_timedelta`

Write a function named `readable_timedelta`. The function should take one argument, an integer<br>`days`, and return a string that says how many weeks and days that is. 
For example, calling the<br>function and printing the result like this:

```
print(readable_timedelta(10))
```

should output the following:

```
1 week(s) and 3 day(s).
```

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_5/timedelta.py)

<br>

## Quiz: Lambda with Map

`map()` is a higher-order built-in function that takes a function and iterable as inputs, 
and returns an<br>iterator that applies the function to each element of the iterable. 
The code below uses `map()` to find<br>the mean of each list in `numbers` to create the list `averages`.

Write this code to be more concise by using a lambda expression defined within the call to `map()`.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_5/mean.py)

<br>

## Quiz: Lambda with Filter

`filter()` is a higher-order built-in function that takes a function and iterable as inputs and returns<br>an iterator 
with the elements from the iterable for which the function returns True.
The code below<br>uses `filter()` to get the names in `cities` that are fewer than 10 characters long to create the list<br>`short_cities`.

Write this code to be more concise by using a lambda expression defined within the call to `filter()`.

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_5/cities.py)
