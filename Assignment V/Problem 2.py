# ASSIGNMENT V - CIS 206 - phil may'r

# Problem 2

full_name = input("Enter full name: ")

first_name, middle_name, last_name = full_name.split()

first_initial = first_name[0]
middle_initial = middle_name[0]
last_initial = last_name[0]

formatted_initials = first_initial + '. ' + middle_initial + '. ' + last_initial + '.'

print("The initials of '" + full_name + "' are '" + formatted_initials + "'")
