def manual_remove(lst, value):
    if value in lst:
        lst.remove(value)
    else:
        print(f"{value} არაა სიაში!")
