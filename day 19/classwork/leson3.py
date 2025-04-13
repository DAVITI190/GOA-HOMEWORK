def join_integers_to_string(arr):
    return ''.join(str(num) for num in arr)

my_list = [1, 2, 4, 18]
result = join_integers_to_string(my_list)
print(result) 
