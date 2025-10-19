# Check if one string is substring of another 

def is_substring(s1, s2):
    n, m = len(s1), len(s2)
    for i in range(n - m + 1):
        if s1[i:i+m] == s2:
            return True
    return False

s1 = input("Enter string: ")
s2 = input("Enter Substring: ")
if is_substring(s1,s2):
    print(f"{s2} is substring of {s1}")
else: 
    print(f"{s2} is not substring of {s1}")
