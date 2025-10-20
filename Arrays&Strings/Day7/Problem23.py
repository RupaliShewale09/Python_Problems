#  Check if two strings are anagrams
#  Anagrams: silent listen

#Solution 1
def check_anagrams_sorted(s1, s2):
    return sorted(s1) == sorted(s2)

#solution 2
def check_anagrams(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    if len(s1) != len(s2):
        return False
    
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1    # update value to value+1 if exist else default 0+1

    for char in s2:
        if char not in count:
            return False
        count[char] -= 1

    #check all counts are zero    
    for value in count.values():
        if value != 0:
            return False
    
    return True

#solution 3
def check_anagrams_freq(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in s1:
        freq1[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq2[ord(ch) - ord('a')] += 1

    return freq1 == freq2

s1 = input("Enter first string:")
s2 = input("Enter second string:")

if check_anagrams_freq(s1, s2):
    print(f"{s1} & {s2} are anagrams")
else:
    print(f"{s1} & {s2} are not anagrams")