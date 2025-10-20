#  Reverse each word in a string
# Enter a sentence: Hello World     
# Reversed string (words): World Hello

#solution 1: using 2 pointer
def reverse_words(s):
    str1 = s.split()

    left = 0
    right = len(str1)-1

    while left < right:
        str1[left], str1[right] = str1[right], str1[left]
        left += 1
        right -= 1

    return ' '.join(str1)

#solution 2 : using another string
def reverse_words2(s):
    reversed_w = ""
    s = s.split()

    for word in s:
        reversed_w = word + " " +reversed_w

    return reversed_w


str = input("Enter a sentence: ")
print("Reversed string (words):", reverse_words(str))
print("Reversed string (words):", reverse_words2(str))