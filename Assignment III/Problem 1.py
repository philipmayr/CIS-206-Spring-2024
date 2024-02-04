# ASSIGNMENT III - CIS 206 - phil may'r

# Problem 1

def get_points():
    return int(input("Enter number of points: "))
    
def get_redemption_code():
    return input("Enter redemption code: ")
    
def compute_points(points, redemption_code):
    if redemption_code == 'C':
        reward_factor = 2.0
    elif redemption_code == 'X':
        reward_factor = 3.0
    else:
        reward_factor = 1.5
    reward_points = points * reward_factor
    return reward_points
    
def print_results(points, redemption_code, reward_points):
    print()
    print("Base Points: " + str(points))
    print("Redemption Code: " + str(redemption_code))
    if reward_points % 1 == 0:
        reward_points = int(reward_points)
    print("Reward Points: " + str(reward_points))

points = get_points()
redemption_code = get_redemption_code()
reward_points = compute_points(points, redemption_code)
print_results(points, redemption_code, reward_points)
    
