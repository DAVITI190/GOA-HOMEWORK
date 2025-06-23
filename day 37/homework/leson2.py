import math

def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

print(is_square(-1)) 
print(is_square(0)) 
print(is_square(3)) 
print(is_square(4))   
print(is_square(25))  
print(is_square(26))  
