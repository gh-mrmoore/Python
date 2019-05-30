"""
Write a function area_of_circle(r) which returns the area of a circle of radius r

As a refresher, the area of any circle is equal to the radius squared, multiplied by pi (where pi is 3.14159....).

Don’t forget to include the math module, where pi is defined.
"""
import math
# TODO: use def to define a function called area_of_circle which takes an argument called r
def area_of_circle(r):
    circle_area = (r ** 2) * math.pi
    
    return circle_area
    
# TODO implement your function to return the area of a circle whose radius is r
def main():
    radius = float(input("For what circle radius would you like to calculate the area?"))

    result = area_of_circle(radius)
    
    print("The area of the circle with radius", radius, "is",result)
    
if __name__ == "__main__":
    main()



# Below are some tests which can give you an indication that your code seems to be correct.

# IMPORTANT: You should NOT include this part when you submit in Vocareum.
# When you submit, only include the function above.

from test import testEqual

t = area_of_circle(0)
testEqual(t, 0)
t = area_of_circle(1)
testEqual(t,math.pi)
t = area_of_circle(100)
testEqual(t, 31415.926535897932)
t = area_of_circle(-1)
testEqual(t, math.pi)
t = area_of_circle(-5)
testEqual(t, 25 * math.pi)
t = area_of_circle(2.3)
testEqual(t, 16.61902513749)
