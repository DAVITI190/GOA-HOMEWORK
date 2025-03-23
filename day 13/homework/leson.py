number = int(input("შეიყვანეთ სამნიშნა რიცხვი: "))

digit_sum = sum(int(digit) for digit in str(number))
remainder = number % digit_sum

print(f"ნაშთი: {remainder}")
