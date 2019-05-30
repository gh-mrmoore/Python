# open the connection to the file that we'll be using
tfile = open("mystery.txt", "r")

#create the turtle we'll use and create the screen
import turtle                                    # allows us to use the turtles library
wn = turtle.Screen()                             # creates a graphics window
wn.bgcolor("gray")                               # set the screen background color
mysti = turtle.Turtle()                          # create a turtle named alex
mysti.pensize(8)                                 # set the size of the pen

#loop through each line in the data file
for aline in tfile:
    if aline[0] == "U":
        mysti.penup()
    elif aline[0] == "D":
        mysti.pendown()
    else:
        values = aline.split()
        mysti.goto(int(values[0]), int(values[1]))

wn.exitonclick()             # wait for a user click on the canvas

#close the file connection
tfile.close()