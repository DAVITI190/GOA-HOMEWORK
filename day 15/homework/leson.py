numbers = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]

even_sum = sum(num for num in numbers if num % 2 == 0)

odd_count = len([num for num in numbers if num % 2 != 0])

print("ლუწი რიცხვების ჯამი:", even_sum)
print("კენტი რიცხვების რაოდენობა:", odd_count)
