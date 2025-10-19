# Remove a given character from string
# s = Rupali    c = p       output: Ruali

#Using a loop and concatenation
def rem_char(s, c):
    result = ""
    for char in s:
        if char != c:
            result+=char

    return result

# Using list comprehension + join()
def rem(s, c):
    return ''.join([char for char in s if char!=c]) 

# Using built-in replace()
def rep_char(s, c):
    return s.replace(c, "")


s = input("Enter string: ")
c = input("Enter character to remove: ")

print(rem_char(s, c))
print(rem(s, c))
print(rep_char(s, c))



