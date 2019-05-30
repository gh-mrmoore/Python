"""
Assume you have a list of numbers nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]

Write a loop that prints each of the numbers on a new line, like this:

12
10
...etc
Write a second loop that prints each number and its square on a new line, precisely like this:

The square of 12 is 144
The square of 10 is 100
...etc
"""
import math

nums = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for x in nums:
    print(x)

for x in nums:
    print("The square of",x,"is",int(math.pow(x, 2)))