"""
Write a function analyze_text that receives a string as input. Your function should count the number of 
alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the 
letter 'e' (upper or lowercase).

Your function should return an analysis of the text in the form of a string phrased exactly like this:

“The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”

You will need to make use of the isalpha function, which can be used like this

"a".isalpha() # => evaluates to True
"3".isalpha() # => evaluates to False
"&".isalpha() # => False
" ".isalpha() # => False

mystr = "Q"
mystr.isalpha() # => True
"""

def count_letter_e(e_string):
    vowels = "eE"
    e_counter = 0
    for each_char in e_string:
        if each_char in vowels:
            e_counter = e_counter + 1
    return e_counter

def analyze_text(text):
    # Your code here
    
    #Define variables
    total_characters = 0
    total_letter_e = 0
    fixed_string = ''
    string_length = 0

    #move through each character in the string the user enters to determine if it is an alphabetical character or not
    for char in text:
        if char.isalpha():
            string_length = string_length + 1
            fixed_string = fixed_string + char
        else:
            string_length = string_length + 0
            fixed_string = fixed_string

    #count the number of letter e-s
    
    e_counted = count_letter_e(fixed_string)
    
    #calculate the percentage of e
    
    if string_length > 0:
        percent_e = (e_counted / string_length) * 100
    else:
        percent_e = 0
        
    #create the final answer to return to the main function
    
    final_answer = "The text contains " + str(string_length) + " alphabetic characters, of which " + str(e_counted) + " (" + str(percent_e)  + "%) are 'e'."

    return final_answer
    
def main():
    user_string = str(input("Please type in the string of characters you wish to analyze."))
    
    print(analyze_text(user_string))
                        
if __name__ == "__main__":
    main()




# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)
