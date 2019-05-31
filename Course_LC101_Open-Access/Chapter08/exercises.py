"""
#1
Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. 
A call to print_triangular_numbers(5) would produce the following output:

1
3
6
10
15
"""
def print_triangular_numbers(n):
    line = 0
    triangle_printout = ''
    triangle_text = ''
    triangle_sum = 0
    
    while line <= n:
        for i in range(1, n+1):
            triangle_sum = triangle_sum + i
            triangle_text = str(triangle_sum)
            triangle_printout += triangle_text + '\n'
            line = line + 1
        return triangle_printout

def main():
    print(print_triangular_numbers(5))
#    print(find_triangular_sum(5))

if __name__ == "__main__":
    main()


"""
#2
Modify the walking turtle program so that rather than a 90 degree 
left or right turn the angle of the turn is determined randomly at each step.
"""
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
            julia.left(random.randint(0, 360))
        else:
            julia.right(random.randint(0, 360))

        julia.forward(50)

    screen.exitonclick()

if __name__ == "__main__":
    main()


"""
#3
Modify the turtle walk program so that you have two turtles each with a random starting location. 
Keep the turtles moving until one of them leaves the screen.
"""
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
    julius = turtle.Turtle()
    
    screen = turtle.Screen()

    julia.shape('turtle')
    julia.color("red")
    julius.shape('turtle')
    julius.color("blue")
    
    while is_in_screen(screen, julia) and is_in_screen(screen, julius):
        coin = random.randrange(0, 2)
        if coin == 0:
            julia.left(random.randint(0, 360))
            julius.left(random.randint(0, 360))
        else:
            julia.right(random.randint(0, 360))
            julius.right(random.randint(0, 360))

        julia.forward(50)
        julius.forward(50)

    
    screen.exitonclick()

if __name__ == "__main__":
    main()


"""
#4
Modify the previous turtle walk program so that the turtle turns around when it hits the wall or when one turtle collides with another turtle.
"""


"""
#5
Here’s the start of a program for a weight training app that coaches users on how much weight they should lift for each of these three lifts: squat, bench, and deadlift. The program begins by having the user lift only 10 pounds for each lift. Each time they complete a set for a particular lift and say they are ready for the next set, add 10 pounds to the weight of their previous set and print a message that this is the new weight they should lift. The sets are all done for one lift at a time. So, for example, a user might squat 10 pounds, then 20 pounds, then 30 pounds and then say they don’t want to keep doing that lift. In this case, they’ll now get a printed message to bench 10 pounds, and so on and so forth.

Some of the code is already included below, but you will need to fill in the rest of the main function to produce the following functionality:

For each lift, beginning with the squat, the function workout_coach should be called with the name of the lift and the current weight. This function prints a message to the user like the following:

Time to squat 10 pounds! You got this!
Keep calling workout_coach for as long as the user answers “yes” to the following question: “Keep doing the squat? Enter yes for the next set.” (Note that you will need to fill in the name of the lift depending on which lift in the iteration they are on.) You can do something like the following to combine strings and a variable to create the prompt string:

input_prompt = "Keep doing the " + lift + "? Enter yes for the next set."
If the user answers with anything besides “yes” to the above question, then stop calling workout_coach for that particular lift and move on to repeat the above process for the next lift (unless it is the deadlift, which is the last lift and thus once the user decides to stop at this point the program quits).
There is one special case where you should stop calling workout_coach — no matter what the user responds — and that is when the current weight is greater than 200 pounds for the bench. You have not yet talked with a lawyer about your app and you don’t want to get sued if anyone has a mishap, so you’re not going to encourage them to lift more than that amount of weight on the bench press (which is the exercise that, done improperly and without a spotter, causes most gym accidents). It is okay to keep encouraging users to lift more than 200 pounds for the squat and the deadlift, though, so you don’t need to set an upper limit for those lifts.
Here is some example output from a program run:

Time to squat 10 pounds! You got this!
Time to squat 20 pounds! You got this!
Time to bench 10 pounds! You got this!
Time to bench 20 pounds! You got this!
Time to bench 30 pounds! You got this!
Time to deadlift 10 pounds! You got this!
Time to deadlift 20 pounds! You got this!
Time to deadlift 30 pounds! You got this!
Time to deadlift 40 pounds! You got this!
"""


"""
#6
Write a program to remove all the red from an image.
"""
import image

img = image.Image("luther.jpg")

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,2000)   # setDelay(0) turns off animation


print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = 0
        new_green = 255 - p.getGreen()
        new_blue = 255 - p.getBlue()

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()


"""
#7
Write a function to convert the image to grayscale.
"""
import image

img = image.Image("luther.jpg")

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,2000)   # setDelay(0) turns off animation


print(img.getWidth())
print(img.getHeight())

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        greyscale = (p.getRed() + p.getGreen() + p.getBlue()) / 3
        
        if greyscale > 125:
            new_color = 255
        else:
            new_color = 0
        
        new_red = greyscale
        new_green = greyscale
        new_blue = greyscale

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()


"""
#8
Write a function to convert an image to black and white.
"""
import image

img = image.Image("luther.jpg")

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,2000)   # setDelay(0) turns off animation


print(img.getWidth())
print(img.getHeight())

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        greyscale = (p.getRed() + p.getGreen() + p.getBlue()) / 3
        
        if greyscale > 125:
            new_color = 255
        else:
            new_color = 0
        
        new_red = new_color
        new_green = new_color
        new_blue = new_color

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()


"""
#9
Sepia Tone images are those brownish colored images that may remind you of times past. 
The formula for creating a sepia tone is as follows:

new_r = (R × 0.393 + G × 0.769 + B × 0.189)
new_g = (R × 0.349 + G × 0.686 + B × 0.168)
new_b = (R × 0.272 + G × 0.534 + B × 0.131)
"""
import image

img = image.Image("luther.jpg")

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,2000)   # setDelay(0) turns off animation


print(img.getWidth())
print(img.getHeight())

p = img.getPixel(45, 55)
print(p.getRed(), p.getGreen(), p.getBlue())

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = (p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        new_green = (p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        new_blue = (p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()


"""
#10
Write a function to uniformly enlarge an image by a factor of 2 (in other words, make the image twice as wide and twice as tall).
"""
import image

img = image.Image("luther.jpg")

win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,2000)   # setDelay(0) turns off animation


print(img.getWidth())
print(img.getHeight())

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        new_red = (p.getRed() * 0.393 + p.getGreen() * 0.769 + p.getBlue() * 0.189)
        new_green = (p.getRed() * 0.349 + p.getGreen() * 0.686 + p.getBlue() * 0.168)
        new_blue = (p.getRed() * 0.272 + p.getGreen() * 0.534 + p.getBlue() * 0.131)

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

img.draw(win)
win.exitonclick()



"""
#11
After you have scaled an image too much it looks blocky. One way of reducing the blockiness of the image is 
to replace each pixel with the average values of the pixels around it. This has the effect of smoothing out 
the changes in color. Write a function that takes an image as a parameter and smooths the image. Your function 
should return a new image that is the same as the old one but smoothed.
"""


"""
#12
When you scan in images using a scanner they may have lots of noise due to dust particles on the image itself 
or the scanner itself, or the images themselves may be damaged. One way of eliminating this noise is to replace 
each pixel by the median value of the pixels surrounding it. Write a program to do this.
"""



