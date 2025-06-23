quarter = (month - 1) // 3 + 1
def get_quarter(month):
    return (month - 1) // 3 + 1

print(get_quarter(2))   # Output: 1
print(get_quarter(6))   # Output: 2
print(get_quarter(11))  # Output: 4
