number = int(input("შეიყვანეთ რიცხვი: "))

if number % 100 == 0 and number % 400 == 0:
    print("ახალი საუკუნე")
else:
    print("ეს არ არის ახალი საუკუნე")