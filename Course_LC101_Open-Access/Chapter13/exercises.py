"""
#1
We can represent a rectangle by knowing three things: the location of its lower left corner, its width, and its height. Create a class definition for a Rectangle class using this idea. For instance, to create a Rectangle object at location (4,5) with width 6 and height 5, we would do the following:

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
"""

"""
#2
Add the following accessor methods to the Rectangle class: get_width and get_height.
"""

"""
#3
Add a method area to the Rectangle class that returns the area of any instance:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.area(), 50)
"""

"""
#4
Write a perimeter method in the Rectangle class so that we can find the perimeter of any rectangle instance:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.perimeter(), 30)
"""

"""
#5
Write a transpose method in the Rectangle class that swaps the width and the height of any rectangle instance:

r = Rectangle(Point(100, 50), 10, 5)
testEqual(r.width, 10)
testEqual(r.height, 5)
r.transpose()
testEqual(r.width, 5)
testEqual(r.height, 10)
"""

"""
#6
Write a new method called contains in the Rectangle class to test if a Point falls within the rectangle. 
For this exercise, assume that a rectangle at (0,0) with width 10 and height 5 has open upper bounds on 
the width and height, i.e. it stretches in the x direction from [0 to 10), where 0 is included but 10 is 
excluded, and from [0 to 5) in the y direction. So it does not contain the point (10, 2). These tests should pass:

r = Rectangle(Point(0, 0), 10, 5)
testEqual(r.contains(Point(0, 0)), True)
testEqual(r.contains(Point(3, 3)), True)
testEqual(r.contains(Point(3, 7)), False)
testEqual(r.contains(Point(3, 5)), False)
testEqual(r.contains(Point(3, 4.99999)), True)
testEqual(r.contains(Point(-3, -3)), False)
"""

"""
#7
Write a new method called diagonal that will return the length of the diagonal that runs 
from the lower left corner to the opposite corner.
"""

"""
#8
There are some games where we put a rectangular “bounding box” around our sprites in the game. 
We can then do collision detection between, say, bombs and spaceships, by comparing whether their 
rectangles overlap anywhere.

Write a function to determine whether two rectangles collide. Hint: this might be quite a tough 
exercise! Think carefully about all the cases as you code.
"""
