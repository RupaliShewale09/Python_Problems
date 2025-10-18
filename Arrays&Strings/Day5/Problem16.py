# Count vowels and consonants

def count_vowels_conso(s):
    s = s.replace(" ","").lower()

    vowels = 0 
    conso = 0
    
    for char in s:
        if char in 'aeiou':
            vowels +=1
        elif char.isalpha():
            conso += 1

    return vowels, conso

s = input("Enter a string:")
v, c = count_vowels_conso(s)
print(f"Vowels: {v}, Consonants: {c}")