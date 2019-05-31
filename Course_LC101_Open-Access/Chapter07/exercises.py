"""
#1
A farmer is on his way to market with a fox, a chicken, and a bag of corn. 
He must cross a river to get there. On the bank of the river is a boat that 
is big enough only for the farmer and one additional item, so he must take 
the three across one at a time.

If the farmer takes the fox first, the chicken will eat the corn.
If the farmer takes the corn first, the fox will eat the chicken.
If the farmer takes the chicken first, the fox will not eat the corn. 
However, he’ll then have to take either the fox or corn on the next trip, 
and when left alone to return for the final item one of the first two situations will occur.
How can the farmer get all three across without losing one?
"""

"""
#2
You have three boxes that contain some combination of apples and oranges:

One has only apples
One has only oranges
One has both apples and oranges
The boxes have labels signifying each of the three, but each box is mislabeled.

You may ask for one item from one of the boxes to be shown to you. This item will 
be randomly pulled from the box.

How can you figure out the correct labeling of the boxes?
"""

"""
#3
You have a job in the quality control department at a ball factory. A coworker 
left behind 10 boxes of balls. You know that each normal ball weighs 10g, and 
each defective ball weighs 9g. There are nine boxes consisting of only normal 
balls, and one box of only defective balls.

You have a digital scale and can take only one measurement. How can you determine 
which box contains the defective balls?
"""

"""
#4
Fill out the main function below so that you handle two exceptions that may be raised 
by your call to some_function. If this function raises a ValueError, print “value 
error happening now”; if this function raises a UnicodeError, print “unicode error 
happening now”. Make sure your code can handle both errors. (Note: since some_function 
isn’t filled out, neither exception will be raised when you run the program.)
"""
def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def main():
    # Put your exception handling code below
    try:
        some_function()
    except UnicodeError:
        print("Unicode error happening now")
    except ValueError:
        print("Value error happening now")

if __name__ == "__main__":
    main()


"""
#5
Write a function line(n) that returns a line with exactly n hashes.

Example:
print(line(5))

Output:
#####
"""
def line(n):
    tag_loop = ""
    for i in range(n):
        tag_loop = tag_loop + "#"
    
    return tag_loop
    

def main():
    # Put your exception handling code below
    
    
    try:
        tag_count = int(input("How many hash-tags should print?"))
        
        result = line(tag_count)
        
        print("Printing:",result)
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()


"""
#6
Write a function square(n) that returns an n by n square of hashes. Utilize your line function.

Example:
print(square(5))
"""
def line(n):
    tag_loop = ""
    for i in range(n):
        tag_loop = tag_loop + "#"
    
    return tag_loop
    

def main():
    # Put your exception handling code below
    
    
    try:
        tag_count = int(input("How many hash-tags should print?"))
        
        result = line(tag_count)
        
        for i in range(tag_count):
            print("Printing:",result)
        
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()


"""
#7
Write a function rectangle(width, height) that returns a rectangle of the 
width and height given by the parameters. Again, utilize your line function to do this.

Example:
print(rectangle(5, 3))
"""
def line(n):
    line_print = ''
    for i in range(n):
        line_print = line_print + "#"
    
    return line_print

def rectangle (w, h):
    row_print = ''
    for i in range(h):
        row_print += (line(w) + '\n')
    
    return row_print

def main():
    # Put your exception handling code below
    
    try:
        rectangle_width = int(input("Rectangle width?"))
        rectangle_height = int(input("Rectangle height?"))
        
        print(rectangle(rectangle_width, rectangle_height))
        
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()


"""
#8
Write a function stairs(n) that prints the pattern shown below, with height n. 
Again, utilize your line function to do this.

Example:
stairs(5))
"""


"""
#9
Write a function space_line(spaces, hashes) that returns a line with exactly the specified 
number of spaces, followed by the specified number of hashes.

Example:
print(space_line(3,5))
"""
def line(n):
    line_print = ''
    for i in range(n):
        line_print = line_print + "#"
    
    return line_print

def space_line (spaces, hashes):
    row_print = ''
    space_print = ''
    for i in range(spaces):
        space_print += " "
    
    row_print = space_print + (line(hashes))
    return row_print

def main():
    # Put your exception handling code below
    
    try:
        space_count = int(input("Number of spaces?"))
        hash_count = int(input("Number of hashes?"))
        
        print(space_line(space_count, hash_count))
        
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()


"""
#10
Write a function triangle(n) that returns an upright triangle of height n.

Example:
print(triangle(5))
"""
def line(n):
    return n * '#'
    
def spacing(x):
    return x * ' '
    
def stairs (h):
    row_print = ''
    for i in range(h):
        row_print += (spacing(h-i) + line((2*i)+1) + '\n')
    
    return row_print

def main():
    # Put your exception handling code below
    
    try:
        stair_height = int(input("Stair height?"))
        
        print(stairs(stair_height))
        
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()


"""
#11
Write a function diamond(n) that returns a diamond where the triangle formed by the 
top portion has height n. Notice that this means the diamond has 2n - 1 rows.

Example:
diamond(5))
"""
def line(n):
    return n * '#'
    
def spacing(x):
    return x * ' '
    
def diamond_tophalf(h):
    top_row_print = ''
    for i in range(h):
        top_row_print += (spacing(h-i) + line((2*i)+1) + '\n')
    
    return top_row_print

def diamond_bottomhalf(h):
    bottom_row_print = ''
    for i in range(h):
        bottom_row_print += (spacing(i) + line((h+2)-i) + '\n')
    
    return bottom_row_print



#def diamond(r):
#    diamond_tophalf(r)
#    
#    return



def main():
    # Put your exception handling code below
    
    try:
        diamond_top = int(input("Rows in top half of diamond?"))
        
        print(diamond_tophalf(diamond_top))
        print(diamond_bottomhalf(diamond_top))
        
    except Exception:
        print("There was an error")
    finally:
        print("This will print no matter what")
    

if __name__ == "__main__":
    main()

