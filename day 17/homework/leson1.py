def manual_index(lst, value):
    for i, item in enumerate(lst):
        if item == value:
            return i
    raise ValueError(f"{value} არაა სიაში!")
