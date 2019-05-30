# open the connection to the file that we'll be using
score_file = open("studentdata.txt", "r")

#set any global variables we might need

#create any functions we might need

for aline in score_file:
    values = aline.split()
    grade_count = len(values) - 1
    
    grade_counter = 1
    grade_sum = 0

    while grade_count >= grade_counter:
        grade_sum = grade_sum + int(values[grade_counter])
        if grade_counter == 1:
            grade_max = int(values[grade_counter])
        else:
            if int(values[grade_counter]) > grade_max:
                grade_max = int(values[grade_counter])
            else:
                grade_max = grade_max

        if grade_counter == 1:
            grade_min = int(values[grade_counter])
        else:
            if int(values[grade_counter]) < grade_min:
                grade_min = int(values[grade_counter])
            else:
                grade_min = grade_min
        
        print("    The grade in position:", grade_counter, "is: ", values[grade_counter], "type:", type(values[grade_counter]))
        grade_counter += 1
        gpa = grade_sum / grade_count

    print(values[0], "had", grade_count, "grades with a sum of:", grade_sum, " that averages to:", round(gpa, 2))
    print("    Minimum score of:", grade_min, "and a maximum score of:", grade_max)
    print()


#close the file connection
score_file.close()