"""
#1
Add a distance_from_point method that works similar to distance_from_origin except that it takes a Point 
as a parameter and computes the distance between that point and self.
"""

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance_from_point(self, target):
        x_diff = (self.x - target.x)
        y_diff = (self.y - target.y)
        return ((x_diff ** 2) + (y_diff ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

def main():
    p = Point(3, 5)
    q = Point(4, 7)
    
    print(p.distance_from_point(q))

if __name__ == "__main__":
    main()

"""
#2
Add a method reflect_x to the class Point which returns a new Point, one which is the reflection of the point 
across the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
"""

class Point:

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __repr__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def reflect_x(self):
        new_y = (self.y - (self.y * 2))
        new_x = self.x
        return Point(new_x, new_y)
    
def main():
    p = Point(3, 5)

    print(p.reflect_x())

if __name__ == "__main__":
    main()

"""
#3
Add a method slope_from_origin, which returns the slope of the line joining the origin to the point. For example,

The equation for calculating slope between any two points is slope = (Y2 - Y1) / (X2 - X1). Remember that dividing 
by 0 is not allowed, so there are some inputs that will cause your method to fail. Return None when that happens.
"""

"""
#4
Add a method called move that will take two parameters, call them dx and dy. The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)
"""

