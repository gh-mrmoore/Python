"""
#1
Draw a reference diagram for a and b before and after the third line of the following Python code is executed:
"""
a = [1, 2, 3]
b = a[:]
b[0] = 5

"""
#2
Create a list called my_list with the following six items: 76, 92.3, "hello", True, 4, 76. 
Do it with both append and with concatenation, one item at a time.
"""

a1 = 76
a2 = 92.3
a3 = "hello"
a4 = True
a5 = 4
a6 = 76

my_list_append = []
my_list_append.append(a1)
my_list_append.append(a2)
my_list_append.append(a3)
my_list_append.append(a4)
my_list_append.append(a5)
my_list_append.append(a6)

print(my_list_append)

my_list_concatenation = []
my_list_concatenation = my_list_concatenation + [a1]
my_list_concatenation = my_list_concatenation + [a2]
my_list_concatenation = my_list_concatenation + [a3]
my_list_concatenation = my_list_concatenation + [a4]
my_list_concatenation = my_list_concatenation + [a5]
my_list_concatenation = my_list_concatenation + [a6]

print(my_list_concatenation)

"""
#3
Starting with the list in Exercise 2, write Python statements to do the following:

Append “apple” and 76 to the list.
Insert the value “cat” at position 3.
Insert the value 99 at the start of the list.
Find the index of “hello”.
Count the number of 76s in the list.
Remove the first occurrence of 76 from the list.
Remove True from the list using pop and index.
""""

my_list = [76, 92.3, "hello", True, 4, 76]

my_list.append("apple")
my_list.append(76)

print(my_list)

my_list.insert(3, "cat")

print(my_list)

my_list.insert(0,99)

print(my_list)

print(my_list.index("hello"))

print(my_list.count(76))

my_list.remove(76)

print(my_list)

my_list.pop(my_list.index(True))

print(my_list)

"""
#4
Write a function to count how many odd numbers are in a list.
"""
def odd_count(number_list):
    #define the variables that will be needed to work with
    odd_counter = 0
    
    for x in number_list:   #cycle through each item in the list
        if x % 2 == 1:   #determine whether or not the number is odd
            odd_counter = odd_counter + 1   #accumulate the total count of odd numbers
    
    #return the result to the main function
    return odd_counter
    
def main():
    number_list = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    
    print(odd_count(number_list))
    
if __name__ == "__main__":
    main()

"""
#5
Write a Python function that will take a list of 100 random integers between 0 and 1000 
(you can use iteration, append, and the random module to create a test list) and return 
the maximum value. (Note: there is a built-in function named max but do not use it for 
this exercise.)
"""

import random

def find_max(alist):
    #define the variables needed for this function
    
    current_max = 0
    
    for e in alist:
        if e > current_max:
            current_max = e
        else:
            current_max = current_max
    
    #return the maximum value to the main function
    
    return current_max

def main():
    # make a random list to test the function
    alist = []
    for i in range(100):
        alist.append(random.randint(0, 1000))
    
#    for x in alist:
#        print(x)
    
    print(alist)
    print()
    print(find_max(alist))

if __name__ == "__main__":
    main()

"""
#6
Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers 
in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
"""
import random

def sum_of_squares(xs):

    #define the variables that will be needed
    xs_squared = []
    square_sums = 0
    
    #loop thru the list and square each value
    
    for i in range(len(xs)):
        xs[i] = xs[i] ** 2

    #loop thru the squared list and sum the values
    
    for i in range(len(xs)):
        square_sums = square_sums + xs[i]
    
    #return the value to the main function
    
    return square_sums
    
    

def main():
    # make a random list to test the function
    alist = []
    for i in range(5):
        alist.append(random.randint(0, 1000))
    
#    for x in alist:
#        print(x)
    
    print(alist)
    print()
    print(sum_of_squares(alist))

if __name__ == "__main__":
    main()

"""
#7
Sum up all the negative numbers in a list.
"""

import random

def negative_sums(alist):
    #define the variables that will be used
    
    negative_sum = 0
    
    #loop thru the list and determine whether the number is negative
    for x in alist:
        if x < 0:
        #summation of the negative numbers
            negative_sum = negative_sum + x
        else:
            negative_sum = negative_sum
    
    #return the negatives summed up
    
    return negative_sum
            

def main():
    # make a random list to test the function
    alist = []
    for i in range(5):
        alist.append(random.randint(-100, 100))
    
    print(alist)
    print()
    print(negative_sums(alist))

if __name__ == "__main__":
    main()

"""
#8
Count how many words in a list have length 5.
"""

def five_words(wordlist):
    #define the variables that will be used
    
    five_letter_counter = 0
    
    #loop thru the list and determine which items have 5 characters
    for words in wordlist:
        if len(words) == 5:
        #summation of the negative numbers
            five_letter_counter = five_letter_counter + 1
        else:
            five_letter_counter = five_letter_counter
    
    #return the negatives summed up
    
    return five_letter_counter
            

def main():
    # make a list to test the function
    wordlist = ["apple", "banana", "pear", "orange", "fruit", "grape"]
    
    print(wordlist)
    print()
    print(five_words(wordlist))

if __name__ == "__main__":
    main()

"""
#9
Although Python provides us with many list methods, it is good practice and very instructive 
to think about how they are implemented. Implement your own Python functions that works like 
the following built-in ones:

count
in
reverse
index
insert
Note that you cannot call your version of the in function “in”, since that is a reserved keyword. You could call it is_in instead.
"""

"""
#10
Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')
"""

s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"

new_s = s.replace("om", "am")

print(new_s)

"""
#11
Write a function that will sum up all the elements in a list up to but not including the first even number.
"""

def sum_of_initial_odds(nums):
    #define the variables that we'll be using
    first_even_index = 0
    number_index = 0
    summation_index = 0
    summation_result = 0

    #find the index where the first even number appears
    for numbers in nums:
        while first_even_index == 0:
            current_number = int(nums[number_index])
            if current_number % 2 == 0:
                first_even_index = first_even_index + 1
            else:
                first_even_index = first_even_index
                number_index = number_index + 1

    #create a summation of the numbers that appear before the first even number
    number_index = number_index - 1

    for numbers in nums:
        while number_index >= summation_index:
            current_sum_number = int(nums[summation_index])
            summation_result = summation_result + current_sum_number
            summation_index = summation_index + 1
    
    return(summation_result)


from test import testEqual

testEqual(sum_of_initial_odds([1,3,1,4,3,8]), 5)
testEqual(sum_of_initial_odds([6,1,3,5,7]), 0)
testEqual(sum_of_initial_odds([1, -7, 10, 23]), -6)
testEqual(sum_of_initial_odds(range(1,555,2)), 76729)