# Reverse letters of each word in a string individually
# Input:  "Hello World"
# Output: "olleH dlroW"


def reverse_each_word(s):
    words = s.split()  # split sentence into words

    for i in range (len(words)):
        char = list(words[i])       # convert word to list of chars
        left = 0
        right = len(char) - 1

        while left < right:
            char[left], char[right] = char[right], char[left]
            left += 1
            right -= 1

        words[i] = ''.join(char)    # convert back to string

    return ' '.join(words)

def reverse_each_word(sentence):
    result = ""
    word = ""
    for ch in sentence:
        if ch != " ":
            word = ch + word      # build reversed word
        else:
            result += word + " "
            word = ""
    result += word   # add last word
    return result


str = input("Enter a string: ")
print("Reversed string:", reverse_each_word(str))