correct_password = "1234"  # შეგიძლია სურვილისამებრ შეცვალო

entered_password = input("შეიყვანე პაროლი: ")

while entered_password != correct_password:
    entered_password = input("არასწორია! სცადე თავიდან: ")

print("პაროლი სწორია!")
