
numbers = [1, 2, 3, 3, 4, 5]

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1]: 
        removed_value = numbers.pop(i)  
        break

print("ახალი list:", numbers)
