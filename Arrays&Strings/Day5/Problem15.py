# Check if string is palindrome

def check_palindrome(str):
    str = str.replace(" ", "").lower()   
    
    left = 0
    right = len(str) - 1

    while left <= right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

str = input("Enter string: ")
if (check_palindrome(str)):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
