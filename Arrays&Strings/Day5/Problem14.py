#  Reverse each word in a string

def reverse_words(str):
    str1 = str.split()

    left = 0
    right = len(str1)-1

    while left < right:
        str1[left], str1[right] = str1[right], str1[left]
        left += 1
        right -= 1

    return ' '.join(str1)

str = input("Enter a sentence: ")
print("Reversed string (words):", reverse_words(str))