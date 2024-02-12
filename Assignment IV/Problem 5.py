# ASSIGNMENT IV - CIS 206 - phil may'r

# Problem 5

y_n = input("Do you wish to run to the program? Enter yes/no: ")

while (y_n.lower() == 'yes'):
    first_exam_score = int(input("Enter first exam score: "))
    if first_exam_score < 0 or first_exam_score > 100:
        y_n = input("Entry outside valid range. Run program again? Enter yes/no: ")
        continue
    second_exam_score = int(input("Enter second exam score: "))
    if second_exam_score < 0 or second_exam_score > 100:
        y_n = input("Entry outside valid range. Run program again? Enter yes/no: ")
        continue
    total_points = (first_exam_score * 0.6) + (second_exam_score * 0.4)
    print("Total points: " + str(total_points))
    break
