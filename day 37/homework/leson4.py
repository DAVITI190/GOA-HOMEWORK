import math

def find_next_square(sq):
    root = math.isqrt(sq)
    if root * root == sq:
        return (root + 1) ** 2
    return -1

print(find_next_square(121)) 
print(find_next_square(625)) 
print(find_next_square(114)) 