class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

def main():
    myfraction = Fraction(3, 4)
    print(myfraction)

    print(myfraction.get_numerator())
    print(myfraction.get_denominator())

if __name__ == "__main__":
    main()

#---------------------------------------------

def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

print(find_gcd(12, 16))

#----------------------------------------------

def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = find_gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

def main():
    myfraction = Fraction(12, 16)

    print(myfraction)
    myfraction.simplify()
    print(myfraction)

if __name__ == "__main__":
    main()

#------------------------------------------------

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)

ourfraction = myfraction
print(myfraction is ourfraction)

#--------------------------------------------------

def same_fraction(f1, f2):
    return (f1.get_numerator() == f2.get_numerator()) and (f1.get_denominator() == f2.get_denominator())

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print(same_fraction(myfraction, yourfraction))

#-------------------------------------------------

def find_gcd(numerator, denominator):
    while numerator % denominator != 0:
        old_num = numerator
        old_den = denominator

        numerator = old_den
        denominator = old_num % old_den

    return denominator

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = find_gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def add(self,fraction2):

        new_num = self.num * fraction2.den + self.den * fraction2.num
        new_den = self.den * fraction2.den

        common = find_gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

def main():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 4)

    f3 = f1.add(f2)
    print(f3)

if __name__ == "__main__":
    main()

#----------------------------------------------------

class Cat:

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # sleepy cats say prrrr, energized cats say meow!
        if self.tired:
            return "prrrr"
        else:
            return "meow!"
def main():
    tom = Cat()
    print("tom says:", tom.noise())
    tom.sleep()
    print("After sleeping, tom says:", tom.noise())
    tom.eat()
    print("After eating, tom still says:", tom.noise())
    tom.eat()
    print("After eating again, tom says:", tom.noise())

if __name__ == "__main__":
    main()

#-------------------------------------------------------

class Cat:

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # sleepy cats say prrrr, energized cats say meow!
        if self.tired:
            return "prrrr"
        else:
            return "meow!"

class Tiger:

    def __init__(self):
        # every Tiger comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Tiger always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Tiger sleepy
            self.tired = True

    def angry(self):
        # a Tiger is angry whenever it is both hungry and tired
        return self.tired and self.hungry

    def noise(self):
        if self.angry():
            # angry Tigers say GRRRR!
            return "GRRRR!"
        elif self.tired:
            return "prrrr"
        else:
            return "meow!"

def main():
    hobbes = Tiger()
    print("hobbes says:", hobbes.noise())
    hobbes.sleep()
    print("After sleeping, hobbes says:", hobbes.noise())
    hobbes.eat()
    print("After eating, hobbes still says:", hobbes.noise())
    hobbes.eat()
    print("After eating again, hobbes says:", hobbes.noise())

if __name__ == "__main__":
    main()

#------------------------------------------------------------

class Cat:

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # sleepy cats say prrrr, energized cats say meow!
        if self.tired:
            return "prrrr"
        else:
            return "meow!"


class Tiger(Cat): # notice the (Cat) in parentheses

    def angry(self):
        # a Tiger is angry whenever it is both hungry and tired
        return self.tired and self.hungry

    def noise(self):
        if self.angry():
            # an angry Tiger says GRRRR!
            return "GRRRR!"
        else:
            # a non-angry Tiger behaves like a Cat
            return Cat.noise(self)

def main():
    hobbes = Tiger()
    print("hobbes says:", hobbes.noise())
    hobbes.sleep()
    print("After sleeping, hobbes says:", hobbes.noise())
    hobbes.eat()
    print("After eating, hobbes still says:", hobbes.noise())
    hobbes.eat()
    print("After eating again, hobbes says:", hobbes.noise())

if __name__ == "__main__":
    main()

#-----------------------------------------------------------

class Cat:

    def __init__(self):
        # every Cat comes into this world tired and hungry
        self.tired = True
        self.hungry = True

    def sleep(self):
        self.tired = False
        # a Cat always wakes up hungry
        self.hungry = True

    def eat(self):
        if self.hungry:
            self.hungry = False
        else:
            # eating when already full makes a Cat sleepy
            self.tired = True

    def noise(self):
        # sleepy cats say prrrr, energized cats say meow!
        if self.tired:
            return "prrrr"
        else:
            return "meow!"

class HouseCat(Cat):

    def __init__(self, name):
        # first, initialize as a normal Cat
        Cat.__init__(self)
        # then set the name attribute
        self.name = name

    def satisfied(self):
        return not self.hungry and not self.tired

    def noise(self):
        if self.satisfied():
            return "Hello, my name is " + self.name + "!"
        else:
            return Cat.noise(self)

def main():
    garfield = HouseCat("Garfield")
    print("garfield says:", garfield.noise())
    garfield.sleep()
    print("After sleeping, garfield says:", garfield.noise())
    garfield.eat()
    print("After eating, garfield says:", garfield.noise())
    garfield.eat()
    print("After eating again, garfield says:", garfield.noise())

if __name__ == "__main__":
    main()

#--------------------------------------------------------

import turtle

class StarTurtle(turtle.Turtle):

    def star(self, numpoints, radius):
        for i in range(0, numpoints):
            self.forward(radius)
            self.back(radius)
            self.left(360 / numpoints)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = StarTurtle()
    tess.color("hotpink")

    # draw a star
    tess.star(7, 60)

    # move somewhere else
    tess.penup()
    tess.forward(30)
    tess.left(45)
    tess.pendown()

    # draw another star
    tess.color("blue")
    tess.star(15, 45)

    # and one more
    tess.color("yellow")
    tess.star(15, 30)

if __name__ == "__main__":
    main()

#-------------------------------------------------

