def most_common_type(lst):
    type_counts = {}

    for item in lst:
        item_type = type(item)
        if item_type in type_counts:
            type_counts[item_type] += 1
        else:
            type_counts[item_type] = 1
