def sum_two_numbers(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "შეყვანილი მონაცემები არ არის რიცხვები"
