while True:
    number = int(input("შეიყვანეთ რიცხვი 50-ის ჩათვლით: "))
    if number <= 50:
        break
    else:
        print("გთხოვთ შეიტანოთ რიცხვი რომელიც იქნება 50 ან ნაკლები.")

print(f"{number} - ის ჯერადები 100-ის ჩათვლით:")
for i in range(1, 101):
    if i % number == 0:
        print(i)