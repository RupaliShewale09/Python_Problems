# Count vowels and consonants

def count_Vowels_conso(s):
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
print("The count of vowels and consonents : ", count_Vowels_conso(s))