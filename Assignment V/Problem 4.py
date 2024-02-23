# ASSIGNMENT V - CIS 206 - phil may'r

# Problem 4

def find_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for index, char in enumerate(string):
        if char.lower() in vowels:
            vowel_count += 1
        if char.lower() == 'y':
            if index == len(string) - 1:
                vowel_count += 1
            elif not (string[index + 1].isalpha()):
                vowel_count += 1
            elif not (index == 0) and 
                 not (string[index - 1] in vowels) and 
                 not (string[index + 1] in vowels):
                vowel_count += 1
                
    return vowel_count
        
def find_consonants(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    for char in string:
        if char.lower() not in vowels and char.isalpha():
            consonant_count += 1
                
    return consonant_count
                
string = input("Please enter a string of characters: ")

vowel_count = find_vowels(string)
consonant_count = find_consonants(string)

print("The input string contains " + str(vowel_count) + " vowels and " +
                                     str(consonant_count) + " consonants.")
