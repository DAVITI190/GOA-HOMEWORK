def count_vowels(s):
    return sum(1 for char in s if char in 'aeiou')

print(count_vowels("hello world"))  
print(count_vowels("this is a test"))  
print(count_vowels("sky"))         
