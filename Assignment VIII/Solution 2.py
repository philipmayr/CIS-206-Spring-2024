# ASSIGNMENT VIII - CIS 206 - phil may'r

# Problem 2

series = []

print("Enter 20 numbers below: ")

for i in range(0, 20):
    series.append(float(input()))
    
smallest_number = min(series)
largest_number = max(series)
total_of_numbers = sum(series)
average_number = total_of_numbers / len(series)

print()

print("The smallest number in the list is: " + str(smallest_number))
print("The largest number in the list is: " + str(largest_number))
print("The total of the numbers in the list is: " + str(total_of_numbers))
print("The average of the numbers in the list is: " + str(average_number))
