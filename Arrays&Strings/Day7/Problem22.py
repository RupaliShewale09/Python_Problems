# Remove all vowels from string 

def rm_vowels(s):
    return ''.join([char for char in s if char not in 'aeiouAEIOU'])

def rm_vowels2(s):
    for char in 'aeiouAEIOU':
        s = s.replace(char, '')
    return s

s = input("Enter string: ")
print("New string (method 1):", rm_vowels(s))
print("New string (method 2):", rm_vowels2(s))
