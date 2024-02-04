# ASSIGNMENT III - CIS 206 - phil may'r

# Problem 2

def perform_operation(first_num, second_num, operation_code):
    if operation_code == 'A':
        result = first_num + second_num
    elif operation_code == 'S':
        result = first_num - second_num
    elif operation_code == 'M':
        result = first_num * second_num
    elif operation_code == 'D':
        if second_num == 0:
            result = -999
        else:
            result = first_num / second_num
    return result
    
def display_result(first_num, second_num, operation_code, result):
    print()
    
    # drop whole number mantissas
    if first_num % 1 == 0:
        first_num = int(first_num)
    if second_num % 1 == 0:
        second_num = int(second_num)
    if result % 1 == 0:
        result = int(result)
    
    print("First Number: " + str(first_num))
    print("Second Number: " + str(second_num))
    print("Operation Code: " + operation_code)
    print("Result: " + str(result))
    if second_num == 0 and operation_code == 'D':
        print("Error: Division by Zero Undefined")

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operation_code = input("Enter operation code (A, S, M, D): ")
result = perform_operation(first_num, second_num, operation_code)
display_result(first_num, second_num, operation_code, result)
