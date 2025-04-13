def remove_odd_numbers(arr):
    return [num for num in arr if num % 2 == 0]

my_list = [1, 2, 3, 4, 5, 6, 7]
new_list = remove_odd_numbers(my_list)
print(new_list)  
