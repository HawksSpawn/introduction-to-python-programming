# Quiz Lesson 7

<br>

## Quiz: Implement  `my_enumerate`

Write your own generator function that works like the built-in function `enumerate`.

Calling the function like this:

```
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
```

should output:

```
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
```

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_7/my_enumerate.py)

<br>

## Quiz: Chunker

If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), being<br>able to take and use chunks of it at a time can be very valuable.

Implement a generator function, `chunker`, that takes in an iterable and yields a chunk of a specified<br>size at a time.

Calling the function like this:

```
for chunk in chunker(range(25), 4):
    print(list(chunk))
```

should output:

```
[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
```

[Solution](https://github.com/HawksSpawn/introduction-to-python-programming-solutions/blob/master/assignments/Lesson_7/chunker.py)
