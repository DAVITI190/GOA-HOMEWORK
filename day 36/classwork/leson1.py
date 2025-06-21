def check_vowel(s, n):
    if n < 0 or n >= len(s):
        return False
    return s[n].lower() in 'aeiou'

print(check_vowel('cat', 1))
print(check_vowel('cat', 0))
print(check_vowel('cat', 4))
print(check_vowel('ApplE', 0))
print(check_vowel('dog', -1))
