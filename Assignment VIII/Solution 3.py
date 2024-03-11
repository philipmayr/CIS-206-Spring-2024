def get_midpoint(first_endpoint, second_endpoint):
    x1, y1 = first_endpoint
    x2, y2 = second_endpoint
    x = (x1 + x2) / 2 
    y = (y1 + y2) / 2
    
    midpoint = x, y
    
    return midpoint
    
print("This program finds the midpoint of two endpoints.\n")
first_endpoint_input = input("Enter ordered pair (x1, y1) of first endpoint: ")
second_endpoint_input = input("Enter ordered pair (x2, y2) of second endpoint: ")

x1 = x2 = y1 = y2 = 0

for i in first_endpoint_input:
    numbers = []
    x, y = numbers
    
for i in second_endpoint_input:
    numbers = []
    x, y = numbers

first_endpoint = x1, y1
second_endpoint = x2, y2

midpoint = get_midpoint(first_endpoint, second_endpoint)
