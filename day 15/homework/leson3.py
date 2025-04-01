numbers = [1, 2, 3, 4, 6, 8, 9]

for num in range(1, 10):  
    if num not in numbers:  
        numbers.append(num) 

print("ახალი list:", sorted(numbers))
