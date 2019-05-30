import turtle                # allows us to use the turtles library
wn = turtle.Screen()         # creates a graphics window
alex = turtle.Turtle()       # create a turtle named alex
alex.forward(150)            # tell alex to move forward by 150 units
alex.left(90)                # turn by 90 degrees
alex.forward(75)             # complete the second side of a rectangle


#import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(150)
tess.left(120)
tess.forward(150)

wn.exitonclick()                # wait for a user click on the canvas


#import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()           # create alex

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()


for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")


#import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()


print(list(range(0, 19, 2)))
print(list(range(0, 20, 2)))
print(list(range(10, 0, -1)))


import math

print(math.pi)
print(math.e)

print(math.sqrt(2.0))

print(math.sin(math.radians(90)))   # sin of 90 degrees


import random

prob = random.random()
print(prob)

diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print(diceThrow)


