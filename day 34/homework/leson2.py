def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))
print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))
print(dont_give_me_five(-10, 10))
