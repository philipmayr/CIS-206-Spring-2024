# ASSIGNMENT V - CIS 206 - phil may'r

# Problem 4

# Reference: https://www.woodwardenglish.com/letter-y-vowel-or-consonant/

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
            elif not (index == 0) and \
                 not (string[index - 1] in vowels) and \
                 not (string[index + 1] in vowels):
                vowel_count += 1
                
    return vowel_count
        
def find_consonants(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_count = 0
    for index, char in enumerate(string):
        if char.lower() not in vowels and char.isalpha():
            if char.lower() == "y":
                if index == 0:
                    consonant_count += 1
                    continue
                elif not (index == len(string) - 1):
                    if string[index - 1] in vowels or \
                       string[index + 1] in vowels:
                        consonant_count += 1
                        continue
            if char.lower() != "y":
                consonant_count += 1
                
    return consonant_count
    
# Inf. loop for testing
while(True):       
    string = input("Please enter a string of characters: ")
    
    vowel_count = find_vowels(string)
    consonant_count = find_consonants(string)
    
    print("'" + string + "' contains " + str(vowel_count) + " vowel(s) and " +
                                         str(consonant_count) + " consonant(s).",
                                         end="\n\n")
