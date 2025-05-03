def check_type_match(value, type_name):
    type_map = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "list": list,
        "dict": dict
    }
    
    expected_type = type_map.get(type_name.lower())
    
    if expected_type:
        return isinstance(value, expected_type)
    else:
        return "მიუთითეთ სწორი ტიპის სახელი"
