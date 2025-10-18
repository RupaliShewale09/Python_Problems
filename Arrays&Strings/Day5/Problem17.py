# Compare two strings without using  == 

def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False       
    return True


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if compare_strings(s1, s2):
    print("Strings are equal")
else:
    print("Strings are not equal")
