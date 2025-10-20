# Reverse a string 
# Enter a string: Hello World         
# Reversed string: dlroW olleH

#solution 1: using 2 pointer
def reverse_string(s):
    chars = list(s)
    
    left = 0
    right = len(s) - 1 

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

#solution 2: using another string
def reverse_string2(s):
    reversed_s = ""
    for ch in s:
        reversed_s = ch + reversed_s
    
    return reversed_s


str = input("Enter a string: ")
print("Reversed string:", reverse_string(str))
print("Reversed string:", reverse_string2(str))