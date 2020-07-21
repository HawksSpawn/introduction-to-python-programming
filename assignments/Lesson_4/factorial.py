# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

for current in range(1, number + 1):
    product *= current

print(product)
