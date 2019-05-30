"""
#3
Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).

If it is currently 13 and you set your alarm to go off in 50 hours, the hour will be 15 (3pm). Write a 
program to solve the general version of the above problem. Ask the user for the current time (in hours), 
and then ask for the number of hours to wait for the alarm.

Your program should output what the hour will be on the clock when the alarm goes off.
"""
str_timenow = input("What time is it now?")
timenow = int(str_timenow)
                  
str_alarm_time = input("How many hours to wait until alarm?")
alarm_time = int(str_alarm_time)

alarm_goes_off = (timenow + alarm_time) % 24
print(alarm_goes_off)

"""
#4
Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, 
then print out the sentence on one line using print.
"""
var01 = 'All'
var02 = 'work'
var03 = 'and'
var04 = 'no'
var05 = 'play'
var06 = 'makes'
var07 = 'Jack'
var08 = 'a'
var09 = 'dull'
var10 = 'boy'

print(var01, " ", var02, " ", var03, " ", var04, " ", var05, " ", var06, " ", var07, " ", var08, " ", var09, " ", var10)

"""
#5
Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
"""
print(6 * (1 - 2))

"""
#6
The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

formula for compound interest
Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, 
and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, 
t, that the money will be compounded for. Calculate and print the final amount after t years.
"""
p = 10000
n = 12
r = .08

str_t = input("How many years invested?")
t = int(str_t)

a = p * ((1 + (r/n))**(n*t))

print(a)

"""
#7
Write a program that will compute the area of a circle. Prompt the user to enter the radius, and then print the answer, like this:
What is the radius of your circle?
"""
str_radius = input("What is the radius of your circle?")
radius = float(str_radius)

circle_area = 3.14159 * (radius**2)

print(circle_area)

"""
#8
Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. 
Print a nice message with the answer.
"""
str_length = input("Rectangle length?")
length = float(str_length)

str_height = input("Rectangle height?")
height = float(str_height)

area = length*height

print("The area of the rectangle is",area)

"""
#9
Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. 
Print a nice message with the answer, like this:

How many miles have you driven?
>>> 150
How many gallons have you used?
>>> 5
Your car gets 30 miles per gallon.
"""

str_miles = input("How many miles have you driven?")
miles = float(str_miles)

str_gallons = input("How many gallons of fuel have you used?")
gallons = float(str_gallons)

mileage = miles/gallons

print("Your car gets",mileage,"miles per gallon.")

"""
#10
Write a program that will convert degrees Celsius to degrees Fahrenheit.
"""
#Multiply the Celsius temperature by 9
#Divide the answer by 5
#Add 32

str_celcius = input("What degrees Celcius?")
celcius = float(str_celcius)

fahrenheit = ((celcius*9)/5) + 32

print("It is",fahrenheit,"degrees Fahrenheit.")

"""
#11
Write a program that will convert degrees Fahrenheit to degrees Celsius, like this:
What is the temperature in Fahrenheit?
>>> 32
32.0 degrees Fahrenheit is 0.0 degrees Celsius.
"""
#Subtract 32
#Multiply by 5
#Divide by 9

str_fahr = input("What are the Fahrenheit temperature?")
fahrenheit = float(str_fahr)

celcius = ((fahrenheit-32)*5)/9

print("It is",celcius,"degrees Celcius.")