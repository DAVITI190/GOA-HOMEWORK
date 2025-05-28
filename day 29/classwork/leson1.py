def replace_vowel_codes(arr):
    vowel_codes = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    
    return [vowel_codes[num] if num in vowel_codes else num for num in arr]

input_array = [100, 100, 116, 105, 117, 121]
output_array = replace_vowel_codes(input_array)

print(output_array)



