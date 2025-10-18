# Reverse a string in-place

def reverse_string(str):
    chars = list(str)
    
    left = 0
    right = len(str) - 1 

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

str = input("Enter a string: ")
print("Reversed string:", reverse_string(str))