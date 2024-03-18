# ASSIGNMENT IX - CIS 206 - phil may'r

import re

# Solution 1

test_strings = ["ABCDEFabcdef123450", "*&%@#!}{"]

for test_string in test_strings:
    if re.search("^[a-zA-Z0-9]", test_string):
        print(test_string + " contains only the set of characters a-z, A-Z, and 0-9.")
    else:
        print(test_string + " contains characters outside the set of characters a-z, A-Z, and 0-9.")
    
print("~~~")

# Solution 2

test_strings = ["ab", "abc", "a", "ab", "abb"]

for test_string in test_strings:
    if re.search("ab*", test_string):
        print(test_string)
        
print("~~~")
        
# Solution 3

for test_string in test_strings:
    if re.search("ab+", test_string):
        print(test_string)

# Solution 4        
        
test_strings = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]

for test_string in test_strings:
    if re.search("^[a-z]+_[a-z]+$", test_string):
        print(test_string)
                
print("~~~")

# Solution 5        
        
test_strings = ["The quick brown fox jumps over the lazy dog.", " The quick brown fox jumps over the lazy dog."]

for test_string in test_strings:
    match = re.match(r"^\w+", test_string)
    if match:
        print(match.group())
        
print("~~~")

# Solution 10

test_strings = ["Regular Expressions", "Code_Examples"]

for test_string in test_strings:
    test_string = re.sub('\s', '_', test_string)
    print(test_string)
    
for test_string in test_strings:
    test_string = re.sub('_', ' ', test_string)
    print(test_string)
    
print("~~~")

# Solution 11

test_url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

year = re.search(r"/\d{4}/(?=\d{2}/\d{2}/)", test_url)
year = re.sub('/', '', year.group())

month = re.search(r"(?<=/\d{4})/\d{2}/(?=\d{2}/)", test_url)
month = re.sub('/', '', month.group())

day = re.search(r"(?<=/\d{4}/\d{2})/\d{2}/", test_url)
day = re.sub('/', '', day.group())

print(year)
print(month)
print(day)

print("~~~")

# Solution 12

test_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

matches = re.findall(r"[ae]\w+", test_string)
for match in matches:
    print(match)

print("~~~")

# Solution 13

test_string = "Python Exercises, PHP exercises."

test_string = re.sub(r" |\,|\.",':', test_string)

print(test_string)

print("~~~")

# Solution 14

test_string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

matches = re.findall(r"[ae]\w+", test_string)
for match in matches:
    print(match)

print("~~~")

# Solution 15

test_string = "Python      Exercises"

test_string = re.sub(r" +", ' ', test_string)

print(test_string)
