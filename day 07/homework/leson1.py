number = int(input("შეიყვანეთ რიცხვი: "))

print(f"{number} რიცხვის გამყოფები:")
for i in range(1, number + 1): 
    if number % i == 0:  
        print(i)  
