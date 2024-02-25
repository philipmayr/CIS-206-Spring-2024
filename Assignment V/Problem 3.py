# ASSIGNMENT V - CIS 206 - phil may'r

# Problem 3

def translate_telephone_number(telephone_number):
    letter_dictionary = {
        "A" : 2,
        "B" : 2,
        "C" : 2,
        "D" : 3,
        "E" : 3,
        "F" : 3,
        "G" : 4,
        "H" : 4,
        "I" : 4,
        "J" : 5,
        "K" : 5,
        "L" : 5,
        "M" : 6,
        "N" : 6,
        "O" : 6,
        "P" : 7,
        "Q" : 7,
        "R" : 7,
        "S" : 7,
        "T" : 8,
        "U" : 8,
        "V" : 8,
        "W" : 9,
        "X" : 9,
        "Y" : 9,
        "Z" : 9,
    }
    
    translated_telephone_number = ""
    
    for char in telephone_number:
        if char.isalpha():
            char = letter_dictionary[char]
        translated_telephone_number += str(char)
            
    return translated_telephone_number

telephone_number = input("Enter a 10-character telephone number (XXX-XXX-XXXX): ")
translated_telephone_number = translate_telephone_number(telephone_number)

print("Translated telephone number: " + translated_telephone_number)
