correct_password = "mySecurePassword" 
user_password = input("შეიყვანეთ პაროლი: ")

while user_password != correct_password:
    print("პაროლი არასწორია.")
    user_password = input("შეიყვანეთ პაროლი კვლავ: ")

print("პაროლი სწორია!")