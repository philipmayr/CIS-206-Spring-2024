# ASSIGNMENT III - CIS 206 - phil may'r

# Problem 4

def get_points():
    return int(input("Enter number of points: "))
    
def get_redemption_code():
    return input("Enter redemption code: ")
    
def compute_rewards(points, redemption_code):
    if redemption_code == 'C':
        reward_factor = 2.0
    elif redemption_code == 'X':
        reward_factor = 3.0
    else:
        reward_factor = 1.5
    reward_points = points * reward_factor
    reward_points_dollar_value = reward_points * 1.5
    return reward_points, reward_points_dollar_value
    
def print_rewards(points, redemption_code, reward_points, reward_points_dollar_value):
    print()
    print("Base Points: " + str(points))
    print("Redemption Code: " + str(redemption_code))
    print()
    if reward_points % 1 == 0:
        reward_points = int(reward_points)
    print("Reward Points: " + str(reward_points))
    print("Reward Points Dollar Value: " + "${:,.2f}".format(reward_points_dollar_value))

points = get_points()
redemption_code = get_redemption_code()
reward_points, reward_points_dollar_value = compute_rewards(points, redemption_code)
print_rewards(points, redemption_code, reward_points, reward_points_dollar_value)
