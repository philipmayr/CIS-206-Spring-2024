# ASSIGNMENT VIII - CIS 206 - phil may'r

# Solution 1

print("Enter total rainfall for each of 12 months of year:")

monthly_rainfall = []

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

MONTHS_IN_YEAR = 4

for i in range(0, MONTHS_IN_YEAR):
    while(True):
        try:
            monthly_rainfall.append(float(input()))
            break
        except:
            print("Input invalid, try again:")
    
total_rainfall = sum(monthly_rainfall)
average_rainfall = total_rainfall / len(monthly_rainfall)
highest_rainfall_month = monthly_rainfall.index(max(monthly_rainfall))
lowest_rainfall_month = monthly_rainfall.index(min(monthly_rainfall))

print("Total rainfall over " + str(MONTHS_IN_YEAR) + " months: " + str(total_rainfall))
print("Average rainfall over " + str(MONTHS_IN_YEAR) + " months: " + str(average_rainfall))
print("Month with highest rainfall over " + str(MONTHS_IN_YEAR) + " months: " + months[highest_rainfall_month])
print("Month with lowest rainfall over " + str(MONTHS_IN_YEAR) + " months: " + months[lowest_rainfall_month])
