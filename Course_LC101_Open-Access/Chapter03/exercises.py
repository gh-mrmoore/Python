"""
#1
Below is a short program that prompts the user to input the number of miles they are to drive 
on a given trip and converts their answer to kilometers, printing the result. However, it doesn’t 
work properly. Find and fix the error in the program.
"""
#Original Code
#miles = input("How many miles do you have to drive? ")

#kilometers = miles * 1.60934

#print("That distance is equal to", kilometers, "kilometers")

#Modified Code
miles = input("How many miles do you have to drive? ")

kilometers = float(miles) * 1.60934

print("That distance is equal to", kilometers, "kilometers")

"""
#2
Picture a compass where 0 degrees represents North, 90 degrees represents East, and so on, all 
the way around to 360 degrees, which is again the same as 0 degrees: true north.

The program below envisions the scenario in which a person is facing North (aka 0 degrees) and 
spins some number of rotations, either clockwise or counter-clockwise (-1 represents a full 
counter-clockwise spin and 1 represents a full clockwise spin). It calculates the direction 
they end up facing in degrees. However, it doesn’t work properly. Find and fix the error in the program.
"""

#Original Code
#spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

#degrees = float(spins) * 360

#print("You are facing", degrees, "degrees relative to north")

#Modified Code
spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")

degrees = float(spins) * 360

deflection = degrees % 360

print("You are facing", deflection, "degrees relative to north")

"""
#3
You’ve written a program to convert degrees Celsius to degrees Fahrenheit. 
The program below makes the conversion in the opposite direction, from Fahrenheit to Celsius. 
However, it doesn’t work properly. Find and fix the error in the program.
"""
#Original Code
#current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
#current_temp = int(current_temp_string)

#current_temp_celsius = (current_tmp - 32) * (5/9)
#print("The temperature in Celsius is:", current_temp_celsius)

#Modified Code
current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
current_temp = int(current_temp_string)

current_temp_celsius = (current_temp - 32) * (5/9)
print("The temperature in Celsius is:", current_temp_celsius)

"""
#4
Football Scores Suppose you’ve written the program below. The given program asks the user to input 
the number of touchdowns and field goals scored by an American football team, and prints out the 
team’s score. (We generously assume that for each touchdown, the team always makes the extra point.)

The European Union has decided that they want to start an American football league, and they want 
to use your killer program to calculate scores, but they like things that are multiples of 10 
(e.g. the Metric System), and have decided that touchdowns will be worth 10 points (including 
the extra point they might score) and field goals are worth 5 points. Modify the program below 
to work on both continents, and beyond. It should ask the user how many points a touchdown is 
worth and how many points a field goal is worth. Then it should ask in turn for both the number 
of touchdowns and the number of field goals scored, and then print the team’s total score.
"""
#Original Code
#num_touchdowns = input("How many touchdowns were scored? ")
#num_field_goals = input("How many field goals were scored? ")

#total_score = 7 * int(num_touchdowns) + 3 * int(num_field_goals)

#print("The team has", total_score, "points")

#Modified Code
num_touchdowns = input("How many touchdowns were scored? ")
touchdown_value = input("How many points per touchdown? ")

num_field_goals = input("How many field goals were scored? ")
field_goal_value = input("How many points per field goal?")

total_score = int(touchdown_value) * int(num_touchdowns) + int(field_goal_value) * int(num_field_goals)

print("The team has", total_score, "points")
