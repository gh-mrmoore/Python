# let's define a Point class!
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

#-----------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

# now let's create some Points!
p = Point() # p is a point
q = Point() # q is a different point

print("Nothing seems to have happened with the points")

#---------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()
q = Point()

print(p)
print(q)

print(p is q)

#-----------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, init_x, init_y):
        """ Create a new point at the given coordinates. """
        self.x = init_x
        self.y = init_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


p = Point(7, 6)
print(p.get_x())
print(p.get_y())

#---------------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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


p = Point(7, 6)
print(p.distance_from_origin())

#-------------------------------------------------------------

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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

def distance(point1, point2):
    x_diff = point2.get_x() - point1.get_x()
    y_diff = point2.get_y() - point1.get_y()

    dist = math.sqrt(x_diff**2 + y_diff**2)
    return dist

def main():
    p = Point(4, 3)
    q = Point(0, 0)
    print(distance(p, q))

if __name__=="__main__":
    main()

#----------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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

def main():
    p = Point(7, 6)
    print(p)

if __name__ == "__main__":
    main()

#--------------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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

def main():
    p = Point(7, 6)
    print(p)

if __name__ == "__main__":
    main()

#------------------------------------------------------------

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

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

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

def main():
    p = Point(7, 6)
    print(p)

if __name__ == "__main__":
    main()

#---------------------------------------------------------------

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

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

def main():
    p = Point(3, 4)
    q = Point(5, 12)
    mid = p.halfway(q)

    print(mid)
    print(mid.get_x())
    print(mid.get_y())

if __name__ == "__main__":
    main()

#--------------------------------------------------------------

