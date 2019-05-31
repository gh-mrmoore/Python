"""
#2
Write a function which is given an exam score, and it returns the corresponding letter grade 
as a string according to this scheme:

score	Grade
>= 90	A
[80-90)	B
[70-80)	C
[60-70)	D
< 60	F
The square and round brackets denote closed and open intervals, respectively. A closed 
interval includes the number, an open interval excludes it. So 79.99999 gets grade C , 
but 80 gets grade B.

Test your function by printing the score and the grade for a number of different scores.
"""

def get_grade(x):
    if x >= 90:
        grade = 'A'
    elif 90 > x >= 80:
        grade = 'B'
    elif 80 > x >= 70:
        grade = 'C'
    elif 70 > x >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return grade

def main():
    input_grade = float(input("For what year score would you like the grade?"))

    result = get_grade(input_grade)
               
    print("The score", input_grade, "would get the grade:", result)
    print()

               
if __name__ == "__main__":
    main()

