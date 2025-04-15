def bigger_sum_list(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)

    if sum1 > sum2:
        return list1
    else:
        return list2
