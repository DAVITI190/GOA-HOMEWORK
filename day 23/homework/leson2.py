def combine_strings_and_add_numbers(a, b):
    result = ""
    number_part = ""
    
    for arg in (a, b):
        if isinstance(arg, int):
            number_part += str(arg)
        else:
            result += str(arg)
    
    return result + number_part
