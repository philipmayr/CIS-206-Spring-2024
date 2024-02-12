# ASSIGNMENT IV - CIS 206 - phil may'r

# Problem 2

chances = 3
print("Chances left: " + str(chances))
while (True and chances > 0):
    num = int(input("Enter an integer from 10 to 20, bounds inclusive: "))
    if (num < 10 or num > 20):
        print("Integer outside accepted range.")
        chances -= 1
        print("Chances left: " + str(chances))
        pass
    else:
        break
    
if chances < 1:
    print("Chances used up.")
else:
    for i in range(num + 1):
        print(i)
