import turtle

def draw_square(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()              # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # create alex
draw_square(alex, 50)             # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()


import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()


def square(x):
    y = x * x
    return y

num = 10
result = square(num)
print("The result of ", num, " squared is ", result)


#Considered poor form to access global variable in a function
def bad_square(x):
    y = x ** power
    return y

power = 2
result = bad_square(10)
print(result)


def square(x):
    running_total = 0          # initialize the accumulator!
    for counter in range(x):
        running_total = running_total + x

    return running_total

num = 10
result = square(num)
print("The result of", num, "squared is", result)


def square(i):
    j = i * i
    return j

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c

num_1 = -5
num_2 = 2
num_3 = 10
result = sum_of_squares(num_1, num_2, num_3)
print(result)

num_4 = -2
num_5 = 7
num_6 = 9
result_2 = sum_of_squares(num_4, num_5, num_6)
print(result_2)


def square(n):
    return n * n

def cube(n):
    return n*n*n

def main():
    num = int(input("Please enter a number"))
    print(square(num))
    print(cube(num))

if __name__ == "__main__":
    main()


def daily_miles_traveled(before, after, days):
    total_miles = after - before
    average_miles = total_miles / days
    return average_miles

def reimbursement(miles, pay, extra_pay):
    mileage = miles * pay
    return mileage + extra_pay

def main():
    daily_miles = daily_miles_traveled(1000.0, 1500.5, 5)
    per_mile_pay = .50
    per_diem = 100
    daily_reimbursement = reimbursement(daily_miles, per_mile_pay, per_diem)
    print("Amount you should be reimbursed per day:", daily_reimbursement)

if __name__ == "__main__":
    main()


import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def main():
    data = [48, 117, 200, 240, 160, 260, 220]
    max_height = max(data)
    num_bars = len(data)
    border = 10

    wn = turtle.Screen()             # Set up the window and its attributes
    wn.setworldcoordinates(0-border, 0-border, 40 * num_bars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()           # create tess and set some attributes
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)

    for x in data:
        draw_bar(tess, x)

    wn.exitonclick()

if __name__ == "__main__":
    main()
