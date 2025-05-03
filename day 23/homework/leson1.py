def divide_larger_by_smaller(a, b):
    try:
        a = float(a)
        b = float(b)
        if a == 0 or b == 0:
            raise ZeroDivisionError("გამყოფი არის 0")
        return max(a, b) / min(a, b)
    except ZeroDivisionError as e:
        return str(e)
    except ValueError:
        return "მონაცემები არ არის რიცხვები"
