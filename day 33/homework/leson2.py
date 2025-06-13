def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)
