# ASSIGNMENT VIII - CIS 206 - phil may'r

# Solution 3

# This program is an example of using, packing, and unpacking tuples.
# Currently works with integer coordinate values only.

import re

def find_midpoint(first_endpoint, second_endpoint):
    first_x, first_y = first_endpoint
    second_x, second_y = second_endpoint

    # casting to int so as to drop '.0'
    midpoint_x = int((first_x + second_x) / 2)
    midpoint_y = int((first_y + second_y) / 2)
    
    midpoint = midpoint_x, midpoint_y
    
    return midpoint
    
print("This program will find the midpoint of two endpoints.\n")

first_endpoint = input("Enter ordered pair (x1, y1) of first endpoint: ")
second_endpoint = input("Enter ordered pair (x2, y2) of second endpoint: ")

first_x = second_x = first_y = second_y = 0

for i in first_endpoint:
    # finds integers
    numbers = re.findall('[-]?\d+', first_endpoint)
    first_x, first_y = numbers
        
for i in second_endpoint:
    # finds integers
    numbers = re.findall('[-]?\d+', second_endpoint)
    second_x, second_y = numbers

first_endpoint = int(first_x), int(first_y)
second_endpoint = int(second_x), int(second_y)

midpoint = find_midpoint(first_endpoint, second_endpoint)

print("\n" + str(midpoint) + " is the midpoint of points " + 
             str(first_endpoint) + " and " + 
             str(second_endpoint) + ".")
