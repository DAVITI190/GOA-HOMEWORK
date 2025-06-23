def average(arr):
    if not arr:
        return 0
    return sum(arr) / len(arr)

print(average([1, 2, 3, 4, 5]))  # Output: 3.0
print(average([]))              # Output: 0
