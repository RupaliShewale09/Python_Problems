# palindromic substrings of length 2 or 3 

def print_palindromic_substrings(s):
    n = len(s)
    pals = []
    for i in range(n):
        if (i+1 < n) and (s[i] == s[i+1]):
            pals.append(s[i:i+2])

        if (i+2 < n) and (s[i] == s[i+2]):
            pals.append(s[i:i+3])

    print("Palindromic substrings:", pals)
    print("Count:", len(pals))

s = input("Enter string: ")
print_palindromic_substrings(s)

