# ASSIGNMENT II - CIS 206 - phil may'r

# Problem 2
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
