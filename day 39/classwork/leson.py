def jami(lst):
    i = 0
    total = 0

    while i < len(lst):
        total += lst[i]
        i += 1

    print("რიცხვების ჯამი არის:", total)

jami([4, 7, 10, 3])
