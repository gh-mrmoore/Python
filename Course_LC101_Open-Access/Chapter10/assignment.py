"""
Write a function that will return a string of country codes from an argument that is a string of prices 
(containing dollar amounts following the country codes). Your function will take as an argument a string 
of prices like the following: "US$40, AU$89, JP$200". In this example, the function would return the 
string "US, AU, JP".

Hint: You may want to break the original string into a list, manipulate the individual elements, 
then make it into a string again.
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
