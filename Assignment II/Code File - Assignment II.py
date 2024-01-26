# ASSIGNMENT II - CIS 206 - phil may'r

# Problem 1
print("Enter the lengths of the 3 sides of a triangle below. The program will tell whether the triangle is right, acute, or obtuse.")

side1 = float(input("Enter side 1 length: "))
side2 = float(input("Enter side 2 length: "))
side3 = float(input("Enter side 3 length: "))

side1sq = side1 ** 2
side2sq = side2 ** 2
side3sq = side3 ** 2

if side1sq + side2sq == side3sq:
    print("The triangle is right.")
elif side1sq + side2sq > side3sq:
    print("The triangle is acute.")
elif side1sq + side2sq < side3sq:
    print("The triangle is obtuse.")

# Problem 2

# Problem 3

# Problem 4
print("Enter a year (YYYY) below. The program will tell whether the year is a leap year.")

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year " + str(year) + " is not a leap year.")
        print("The year " + str(year) + " is a leap year.")
    print("The year " + str(year) + " is not a leap year.")
