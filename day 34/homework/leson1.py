def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))
print(reverse_words("This is an example!"))
print(reverse_words("double  spaces"))
