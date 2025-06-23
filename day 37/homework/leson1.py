def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

print(descending_order(42145)) 
print(descending_order(145263))   
print(descending_order(123456789))  
