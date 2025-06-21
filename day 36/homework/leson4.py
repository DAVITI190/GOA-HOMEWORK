def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("abcd"))      # ➞ "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))   # ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))      # ➞ "C-Ww-Aaa-Tttt"
