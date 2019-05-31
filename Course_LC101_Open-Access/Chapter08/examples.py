for guest in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", guest, ". Please come to my party on Saturday")


def sum_to(n):
    sum = 0
    for num in range(1, n+1):
        sum = sum + num

    return sum

print(sum_to(4))

print(sum_to(1000))


def sum_to(n):
    """ Return the sum of 1+2+3 ... n """

    sum = 0
    num = 0

    while num <= n:
        sum = sum + num
        num = num + 1

    return sum

print(sum_to(4))

print(sum_to(1000))


def sum_to(n):
    """ Return the sum of 1+2+3 ... n, up to 100"""

    sum = 0
    num = 0

    while num <= n:
        sum = sum + num
        num = num + 1

        if num > 100:
            break

    return sum

def main():
    print(sum_to(4))
    print(sum_to(100))
    print(sum_to(500))

if __name__ == "__main__":
    main()



def sum_to(n):
    """ Return the sum of odd numbers from 1 to n """

    sum = 0
    num = 0

    while num <= n:
        if num % 2 == 0:
            num = num + 1
            continue

        sum = sum + num
        num = num + 1

    return sum

def main():
    print(sum_to(4))
    print(sum_to(100))

if __name__ == "__main__":
    main()



import random
import turtle

def is_in_screen(screen, t):
    left_bound = - screen.window_width() / 2
    right_bound = screen.window_width() / 2
    top_bound = screen.window_height() / 2
    bottom_bound = -screen.window_height() / 2

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    still_in = True
    if turtle_x > right_bound or turtle_x < left_bound:
        still_in = False
    if turtle_y > top_bound or turtle_y < bottom_bound:
        still_in = False

    return still_in

def main():
    julia = turtle.Turtle()
    screen = turtle.Screen()

    julia.shape('turtle')
    while is_in_screen(screen, julia):
        coin = random.randrange(0, 2)
        if coin == 0:
            julia.left(90)
        else:
            julia.right(90)

        julia.forward(50)

    screen.exitonclick()

if __name__ == "__main__":
    main()


def sequence_3n_plus_one(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""

    while n != 1:

        print(n)

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

    print(n)

sequence_3n_plus_one(3)


import random

def flip_coin():
    """ simulates a coin flip (0 is heads, 1 is tails) """

    coin = random.randrange(0, 2)
    if coin == 0:
        return "heads"
    else:
        return "tails"

def main():
    keep_playing = input("Would you like to flip a coin? If so, enter Yes.")

    while keep_playing == "Yes":
        print(flip_coin())
        keep_playing = input("Would you like to flip a coin? If so, enter Yes.")

    print("Thanks for flipping!")

if __name__ == "__main__":
    main()


print("n", '\t', "2**n")     #table column headings
print("---", '\t', "-----")

for x in range(13):        # generate values for columns
    print(x, '\t', 2 ** x)


