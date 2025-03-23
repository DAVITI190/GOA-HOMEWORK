number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    number += 5
else:
    number *= 3

result = number % 5

print(f"ჯამის 5-ზე ნაშთი: {result}")
