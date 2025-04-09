def manual_pop(lst, index=-1):
    if index < 0:
        index = len(lst) + index  # Negative index support
    if index < 0 or index >= len(lst):
        raise IndexError("ინდექსი სცილდება სიას")
    return lst.pop(index)
