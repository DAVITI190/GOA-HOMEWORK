def get_initials(name):
    names = name.split()
    
    initials = f"{names[0][0].upper()}.{names[1][0].upper()}"
    
    return initials

print(get_initials("Sam Harris"))  
print(get_initials("patrick feeney"))