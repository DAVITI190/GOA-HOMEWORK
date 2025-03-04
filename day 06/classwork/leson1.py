for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if number > 1:
    if is_prime:
        print("Your number is a prime")
    else:
        print("Your number is not a prime")
else:
    print("Your number is not a prime")
number = int(input("Enter a number: "))


if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("Your number is not a prime")
            break
    else:
        print("Your number is a prime")
else:
    print("Your number is not a prime")