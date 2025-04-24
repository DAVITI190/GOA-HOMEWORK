def find_mean(numbers):
    return sum(numbers) / len(numbers)

print(find_mean([1, 3, 5, 7]))  

def find_mean(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)
