answer = 110
guess = 105

if guess < answer:
    result = "Oops! Your guess was too low."
elif guess > answer:
    result = "Oops! Your guess was too high."
elif guess == answer:
    result = "Nice! Your guess matched the answer!"

print(result)
