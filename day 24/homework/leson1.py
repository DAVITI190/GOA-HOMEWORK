def to_alternating_case(string):
    return ''.join(
        char.lower() if char.isupper() else char.upper()
        for char in string
    )
