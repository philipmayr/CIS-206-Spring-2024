# ASSIGNMENT IV - CIS 206 - phil may'r

# Problem 3

fav_names = ["Benjamin", "Caleb", "Daniel", "David", "Jacob", "James", "Jonathan", "Joshua", "Matthew", "Paul"]

name = input("Enter a first name: ")

while (not name in fav_names):
    print("Name not found in list of favorite names. Try again.")
    name = input("Enter a first name: ")
    
print("'" + name + "'" + " found in list of favorite names.")
