"""
Write a course_grader function that takes a list of test scores as its parameter. 
It will add up these test scores and calculate an average score. It should then 
return a message of "pass" or "fail" depending on these two conditions:

If the average score is greater than or equal to 70 and no single test score is 
below 50, then return a message of "pass".

If the average score is lower than 70 or at least one test score is below 50, 
then return a message of "fail".

Some sample function calls with comments on what should be printed out are included 
in main for testing purposes. You should only put the code for the course_grader 
function into Vocareum.
"""

def course_grader(test_scores):
    # Your code here
    
    test_sum = 0
    grade_counter = len(test_scores)

    for score in test_scores:
        if score < 50:
            grade_report = "fail"
            break
        else:
            test_sum = test_sum + score
            grade_avg = test_sum / grade_counter
            
            if grade_avg >= 70:
                grade_report = "pass"
            else:
                grade_report = "fail"

    return grade_report

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
