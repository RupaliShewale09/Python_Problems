# Print all substrings of a string

def print_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

def substrings_com(s):
    n = len(s)
    return [s[i:j] for i in range (n) for j in range(i+1, n+1)]

s = input("Enter string: ")
# print(print_substrings(s))
print(substrings_com(s))

