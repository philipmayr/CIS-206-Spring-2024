# ASSIGNMENT VIII - CIS 206 - phil may'r

# Problem 3

import re

def get_midpoint(first_endpoint, second_endpoint):
    first_x, first_y = first_endpoint
    second_x, second_y = second_endpoint
    
    midpoint_x = (first_x + second_x) / 2.0 
    midpoint_y = (first_y + second_y) / 2.0
    
    midpoint = midpoint_x, midpoint_y
    
    return midpoint
    
print("This program will find the midpoint of two endpoints.\n")

first_endpoint = input("Enter ordered pair (x1, y1) of first endpoint: ")
second_endpoint = input("Enter ordered pair (x2, y2) of second endpoint: ")

first_x = second_x = first_y = second_y = 0

for i in first_endpoint:
    numbers = re.findall('[-]?\d+', first_endpoint)
    first_x, first_y = numbers
        
for i in second_endpoint:
    numbers = re.findall('[-]?\d+', second_endpoint)
    second_x, second_y = numbers

first_endpoint = int(first_x), int(first_y)
second_endpoint = int(second_x), int(second_y)

midpoint = get_midpoint(first_endpoint, second_endpoint)

print("\n" + str(midpoint) + " is the midpoint of points " + 
             str(first_endpoint) + " and " + 
             str(second_endpoint) + ".")
