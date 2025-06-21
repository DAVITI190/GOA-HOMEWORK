def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

print(is_triangle(1, 2, 2))
print(is_triangle(4, 2, 3))
print(is_triangle(2, 2, 2))
print(is_triangle(1, 2, 3))
print(is_triangle(-5, 1, 3))
print(is_triangle(0, 2, 3))
print(is_triangle(1, 2, 9))  
