def remove_non_int_if_only_one(lst):
    
    non_ints = [x for x in lst if not isinstance(x, int) or isinstance(x, bool)]

    if len(non_ints) == 1:
        return [x for x in lst if isinstance(x, int) and not isinstance(x, bool)]
    else:
        return lst