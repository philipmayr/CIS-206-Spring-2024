# ASSIGNMENT IV - CIS 206 - phil may'r

# Problem 1

while (True):
    num = int(input("Enter an integer from 10 to 20, bounds inclusive: "))
    if (num < 10 or num > 20):
        print("Integer outside accepted range.")
        pass
    else:
        break
    
for i in range(num + 1):
    print(i)
