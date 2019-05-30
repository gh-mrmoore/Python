"""
#1
Write a program that prints We like Python's turtles! 1000 times.

Now, update that program to prompt the user for an integer and then 
print the same message the given number of times.
"""
for x in range(10):
    print("We like Python's turtles! ", x)

total_turtles = int(input("Please tell us how may times to print the message"))
for y in range(total_turtles):
    print("We like Python's turtles! ", y)


"""
#2
Write a program that prints out the lyrics to the song “99 Bottles of Beer on the Wall”
"""
for z in range(5, 0, -1):
    print(z, " bottles of beer on the wall, ", z, " bottles of beer.")
    print("--You take one down, you pass it around, ", z-1, " bottles of beer on the wall")


"""
#3
Write a program that prints even integers from 0 to 50.
"""
for a in range(0, 52, 2):
    print(a)


"""
#4
Write a program that uses a for loop to print
One of the months of the year is January
One of the months of the year is February
One of the months of the year is March
etc ...
"""
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    print("One of the months of the year is", month)


"""
#5
Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

An equilateral triangle
A square
A hexagon (six sides)
An octagon (eight sides)
"""
import turtle                # allows us to use the turtles library
wn = turtle.Screen()         # creates a graphics window
myturtle = turtle.Turtle()

#draw triangle
for a in range(3):
    myturtle.forward(25)
    myturtle.left(120)

myturtle.penup()
myturtle.forward(50)
myturtle.pendown()

#draw square
for b in range(4):
    myturtle.forward(25)
    myturtle.left(90)

myturtle.penup()
myturtle.forward(50)
myturtle.pendown()

#draw hexagon
for c in range(6):
    myturtle.forward(25)
    myturtle.left(60)

myturtle.penup()
myturtle.forward(50)
myturtle.pendown()

#draw octagon
for d in range(8):
    myturtle.forward(25)
    myturtle.left(45)

wn.exitonclick()

"""
#6
Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon.
"""


"""
#7
A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes 
another 100 steps, turns another random amount, etc. A social science student records the angle of 
each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. 
(Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.
"""
import turtle                # allows us to use the turtles library
wn = turtle.Screen()         # creates a graphics window
myturtle = turtle.Turtle()

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    myturtle.forward(100)
    myturtle.left(i)

wn.exitonclick()

"""
#8
On a piece of scratch paper, trace the the path of the turtle in the following program. When you are done, press run and check your answer.
"""
import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
tess.speed(5)
tess.right(90)
tess.left(3600)
tess.right(-90)
tess.left(3600)
tess.forward(-100)
wn.exitonclick()


"""
#9
Write a program to look like a regular 5-pointed star.
"""
import turtle                # allows us to use the turtles library
wn = turtle.Screen()         # creates a graphics window
myturtle = turtle.Turtle()

#draw star
for a in range(5):
    myturtle.forward(100)
    myturtle.right(144)

wn.exitonclick()


"""
#10

"""