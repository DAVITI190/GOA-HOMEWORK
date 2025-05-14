def multiply_by_five_power_digits(n):
    num_digits = len(str(abs(n))) if n != 0 else 1
    return n * (5 ** num_digits)
