check_prime = [26, 39, 51, 53, 57, 79, 85]

for number in check_prime:
    for i in range(2, number):
        if number % i == 0:
            print("[{}] is not a prime number".format(number))
            break
        
    if i == number - 1:
        print("[{}] is a prime number".format(number))
