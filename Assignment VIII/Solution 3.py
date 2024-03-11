# ASSIGNMENT VIII - CIS 206 - phil may'r

# Solution 3

# This program is an example of using, packing, and unpacking tuples.

# Reference: 
# https://stackoverflow.com/a/4703409

import re

def find_midpoint(first_endpoint, second_endpoint):
    # unpack tuples
    first_x, first_y = first_endpoint
    second_x, second_y = second_endpoint

    midpoint_x = (first_x + second_x) / 2
    midpoint_y = (first_y + second_y) / 2

    # pack tuple
    midpoint = midpoint_x, midpoint_y

    # return tuple
    return midpoint
    
print("This program will find the midpoint of two endpoints.\n")

first_endpoint = input("Enter ordered pair (x1, y1) of first endpoint: ")
second_endpoint = input("Enter ordered pair (x2, y2) of second endpoint: ")

first_x = second_x = first_y = second_y = 0

for i in first_endpoint:
    numbers = re.findall("[-]?(?:\d*\.*\d+)", first_endpoint)
    first_x, first_y = numbers
        
for i in second_endpoint:
    numbers = re.findall("[-]?(?:\d*\.*\d+)", second_endpoint)
    second_x, second_y = numbers

# pack tuples
first_endpoint = float(first_x), float(first_y)
second_endpoint = float(second_x), float(second_y)

# call function, passing in tuple arguments thereto, initialize variable with function call's tuple return value
midpoint = find_midpoint(first_endpoint, second_endpoint)

# print string representations of tuples
print("\n" + str(midpoint) + " is the midpoint of points " + 
             str(first_endpoint) + " and " + 
             str(second_endpoint) + ".")
