"""
#1
Write a program that allows the user to enter a string. It then prints a table of the letters 
of the alphabet in alphabetical order which occur in the string together with the number of 
times each letter occurs. Case should be ignored. A sample run of the program might look like this:

Please enter a sentence: ThiS is a String with Upper and lower case Letters.
a  3
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$
"""

"""
#2
Write a program that will function as a grade book, allowing a user (a professor or teacher) to enter 
the class roster for a course, along with each student’s cumulative grade. It then prints the class 
roster along with the average cumulative grade. Grades are on a 0-100 percentage scale. Use 2 lists 
(grades and students) and the enumerate function in your solution.

A test run of this program would yield the following:
"""

"""
#3
Implement the functionality of the above program using a dictionary instead of a list.
"""

"""
#4
Make a dictionary where the key is a worker’s name, and the value is a list where the first element 
is the clock in time, second element is the clock out time, and the third element is the total hours 
worked that day. Each worker’s list starts at [0, 0, 0]. Create functions for clock_in and clock_out.

clock_in takes the dictionary of workers, the name of the worker, and the clock in time as parameters. 
When the worker clocks in, enter and save their clock in time as the first element in the associated 
list value.

clock_out takes the same parameters, but with a clock out time instead of clock in time. When the worker 
clocks out, enter and save their clock out time and calculate the hours worked for that day and store 
it as the third element in the list.

To make this program a little easier, we’re entering the clock in and clock out times as integers. 
As a bonus mission, try adding the times as strings representing the 24 hour clock (e.g., "08:00"), 
and then figure out how to calculate the time worked. And you can do this exercise either by aliasing 
or copying the dictionary.
"""

"""
#5
Here’s a table of English to Pirate translations:

English	Pirate
sir	matey
hotel	fleabag inn
student	swabbie
boy	matey
madam	proud beauty
professor	foul blaggart
restaurant	galley
your	yer
excuse	arr
students	swabbies
are	be
lawyer	foul blaggart
restroom	th’ head
my	me
hello	avast
is	be
man	matey

Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.
"""

"""
#6
Give the Python interpreter’s response to each of the following from a continuous interpreter session:

>>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
>>> d['bananas']
>>> d['oranges'] = 20
>>> len(d)
>>> 'grapes' in d
>>> d['pears']
>>> d.get('pears', 0)
>>> fruits = d.keys()
>>> sorted(fruits)
>>> print(fruits)
>>> del d['apples']
>>> 'apples' in d
Be sure you understand why you get each result. Then apply what you have learned to fill in the body of the function below:
"""

