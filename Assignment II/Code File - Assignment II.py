# ASSIGNMENT II - CIS 206 - phil may'r

# Problem 1
print("Enter the lengths of the 3 sides of a triangle below. The program will tell whether the triangle is right, acute, or obtuse.")
print()

side1 = float(input("Enter side 1 length: "))
side2 = float(input("Enter side 2 length: "))
side3 = float(input("Enter side 3 length: "))

side1sq = side1 ** 2
side2sq = side2 ** 2
side3sq = side3 ** 2

print()

if side1sq + side2sq == side3sq:
    print("The triangle is right.")
elif side1sq + side2sq > side3sq:
    print("The triangle is acute.")
elif side1sq + side2sq < side3sq:
    print("The triangle is obtuse.")

# Problem 2
print("\n\t\t··· ··· ···\n")
print("This program mimics a calculator.")
print()

real_num_1 = float(input("Enter first real number: "))
real_num_2 = float(input("Enter second real number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case '+':
        result = real_num_1 + real_num_2
    case '-':
        result = real_num_1 - real_num_2
    case '*':
        result = real_num_1 * real_num_2
    case '/':
        if real_num_2 == 0:
            print("Division by zero undefined.")
            sys.exit()
        else:
            result = real_num_1 / real_num_2
            
# drop mantissa (.0) for whole numbers (formatting)
if real_num_1 % 1 == 0:
    real_num_1 = int(real_num_1)
if real_num_2 % 1 == 0:
    real_num_2 = int(real_num_2)
if result % 1 == 0:
    result = int(result)
        
print("\n" + str(real_num_1) + " " + operator + " " + str(real_num_2) + 
      " is equal to " + str(result) + ".")

# Problem 3
print("\n\t\t··· ··· ···\n")
print("This program finds the best option to choose for author remuneration from three publisher's options.")
print()

# first option consts
DELIVERY_OF_FINAL_MANUSCRIPT_REMUNERATION = 5000
PUBLISHING_REMUNERATION = 20000

# second option const
REMUNERATION_FACTOR_PER_NET_PRICE_COPY = 0.125

# third option consts
REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K = 0.10
REMUNERATION_FACTOR_PER_NET_PRICE_COPY_OVER_4k = 0.14

# get net price per copy and number of copies
net_price_per_copy = float(input("Enter net price per copy: $"))
estimated_num_of_copies = float(input("Enter estimated number of copies to be sold: "))

# find first option total remuneration
FIRST_OPTION_TOTAL_REMUNERATION = DELIVERY_OF_FINAL_MANUSCRIPT_REMUNERATION + \
                                  PUBLISHING_REMUNERATION
      
# find second option total remuneration
SECOND_OPTION_TOTAL_REMUNERATION = net_price_per_copy * \
                                   REMUNERATION_FACTOR_PER_NET_PRICE_COPY * \
                                   estimated_num_of_copies

# find third option total remuneration
if estimated_num_of_copies > 4000:
    THIRD_OPTION_TOTAL_REMUNERATION = (net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K * \
    estimated_num_of_copies) + \
    (net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_OVER_4k * \
    (estimated_num_of_copies - 4000))
else:
    THIRD_OPTION_TOTAL_REMUNERATION = net_price_per_copy * \
    REMUNERATION_FACTOR_PER_NET_PRICE_COPY_FIRST_4K * \
    estimated_num_of_copies
    
# find best option
if (FIRST_OPTION_TOTAL_REMUNERATION >= SECOND_OPTION_TOTAL_REMUNERATION) and \
   (FIRST_OPTION_TOTAL_REMUNERATION >= THIRD_OPTION_TOTAL_REMUNERATION):
   best_option = "first option"
elif (SECOND_OPTION_TOTAL_REMUNERATION >= FIRST_OPTION_TOTAL_REMUNERATION) and \
     (SECOND_OPTION_TOTAL_REMUNERATION >= THIRD_OPTION_TOTAL_REMUNERATION):
   best_option = "second option"
else:
   best_option = "third option"
    
# print results
print()
print("For the first option, the total remuneration amounts to: "
      + '${:,.2f}'.format(FIRST_OPTION_TOTAL_REMUNERATION))  
print("For the second option, the total remuneration amounts to: "
      + '${:,.2f}'.format(SECOND_OPTION_TOTAL_REMUNERATION))   
print("For the third option, the total remuneration amounts to: "
      + '${:,.2f}'.format(THIRD_OPTION_TOTAL_REMUNERATION))  
print()
print("The best option to choose is the " + best_option + ".")

# Problem 4
print("\n\t\t··· ··· ···\n")
print("Enter a year (YYYY) below. The program will tell whether or not the year is a leap year.")
print()

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year " + str(year) + " is not a leap year.")
        print("The year " + str(year) + " is a leap year.")
    print("The year " + str(year) + " is not a leap year.")
