"""
#2
Write a program to draw this (concentric squares). Assume the innermost square is 20 units per side 
and each successive square is 20 units bigger, per side, than the one inside it.
"""
import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    alex.pensize(3)
    
    size = 20

    for i in range(5):
        draw_square(alex,size)
        alex.penup()
        alex.left(180)
        alex.forward(10)
        alex.left(90)
        alex.forward(10)
        alex.left(90)
        alex.pendown()
        size = size + 20

    wn.exitonclick()

if __name__ == "__main__":
    main()

"""
#3
Write a non-fruitful function draw_poly(t, sides, side_length) which makes a turtle draw a regular polygon. 
When called with draw_poly(tess, 8, 50), it will draw a shape like this:
"""
import turtle

def draw_poly(t, sides, side_length):
    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(3)
    
    draw_poly(tess, 8, 50)
    
    wn.exitonclick()


if __name__ == "__main__":
    main()


"""
#4
The two spirals in this picture differ only by the turn angle. Draw both.

Note: Because this program might receive a TimeLimitError we’ve added some code to our answer to 
make the turtle go faster (use its speed method) and to increase the time the program is allowed 
to run to 35 seconds. You can do the latter in your code using:

import sys
sys.setExecutionLimit(35000)
"""
import turtle
import sys

sys.setExecutionLimit(35000)

def draw_spiral(t, angle, sides):
    arm_length = 5
    for i in range(sides):
        t.forward(arm_length)
        t.right(angle)
        t.speed(10)
        arm_length = arm_length + 2

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    thomas = turtle.Turtle()
    thomas.color("blue")
    thomas.pensize(1)
    
    draw_spiral(thomas, 90, 50)
    
    thomas.penup()
    thomas.home()
    thomas.forward(100)
    thomas.pendown()
    
    draw_spiral(thomas, 89, 50)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()


"""
#6
Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. 
So sum_to(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.
"""
def sum_to(n):
    # your code here
    for i in range(n):
        return (n * (n + 1)) / 2
    
def main():
    up_to = int(input("What number would you like to calculate to?"))
    
    result = sum_to(up_to)
    
    print("The result is",result)

    
        
if __name__ == "__main__":
    main()
