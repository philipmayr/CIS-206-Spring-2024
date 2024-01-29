# ASSIGNMENT II - CIS 206 - phil may'r

# Problem 4
print("Enter a year (YYYY) below. The program will tell whether or not the year is a leap year.")

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year " + str(year) + " is not a leap year.")
        print("The year " + str(year) + " is a leap year.")
    print("The year " + str(year) + " is not a leap year.")
