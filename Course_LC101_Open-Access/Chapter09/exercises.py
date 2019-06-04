"""
#1
What is the result of each of the following:

‘Python’[1]
“Strings are sequences of characters.”[5]
len(“wonderful”)
‘Mystery’[:4]
‘p’ in ‘Pineapple’
‘apple’ in ‘Pineapple’
‘pear’ not in ‘Pineapple’
‘apple’ > ‘pineapple’
‘pineapple’ < ‘Peach’
"""

"""
#2
Write a function that will return the number of digits in an integer.
"""

def integer_count(text):

    #Define variables

    #Send the result back to the 'main' function
    return len(text)   #use len function to find the length


def main():
    user_integer = str(input("Please type in the string of characters you wish to analyze."))

    print(integer_count(user_integer))
                        
if __name__ == "__main__":
    main()

"""
#3
Write a function that removes the first occurrence of a string from another string.
"""

from test import testEqual

def remove(substr,original_string):
    # your code here
    
    no_substr = original_string.replace(substr,'',1)
    
    return no_substr

    

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')

"""
#4
Write a function reverse that receives a string argument, and returns a reversed version of the string.
"""

#from test import testEqual

def reverse(text):
    # your code here
    
    #establish variables that will be needed
    reverse_text = ''
    string_length = -1
    
    #loop thru each string to reverse it
    for each_char in text:
        new_character = text[string_length]
        string_length = string_length - 1
        reverse_text = reverse_text + new_character
    
    
    return reverse_text

def main():
    user_string = str(input("Please type in the string of characters you wish to analyze."))
    
    print(reverse(user_string))
                        
if __name__ == "__main__":
    main()

#testEqual(reverse("happy"), "yppah")
#testEqual(reverse("Python"), "nohtyP")
#testEqual(reverse(""), "")

"""
#5
Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!).
"""
from test import testEqual

def reverse(text):
    # your code here
    
    #establish variables that will be needed
    reverse_text = ''
    string_length = -1
    
    #loop thru each string to reverse it
    for each_char in text:
        new_character = text[string_length]
        string_length = string_length - 1
        reverse_text = reverse_text + new_character
    
    
    return reverse_text

def is_palindrome(text):
    # your code here
    
    #establish variables that will be needed
    is_palindrome_string = ''
    
    #get the reverse of the incoming string
    reverse(text)
    
    #connect the original string with the reversed string
#    is_palindrome_string = text + reverse(text)

    #determine whether there is a palindrome
    
    if text == reverse(text):
        palindrome_result = True
    else:
        palindrome_result = False
    
    return palindrome_result


def main():
    user_string = str(input("Please type in the string of characters you wish to analyze."))
    
    print(is_palindrome(user_string))
                        
if __name__ == "__main__":
    main()

    
    
    
testEqual(is_palindrome('abba'), True)
testEqual(is_palindrome('abab'), False)
testEqual(is_palindrome('straw warts'), True)
testEqual(is_palindrome('a'), True)
testEqual(is_palindrome(''), True)

"""
#6
Write a function that mirrors its argument. For example, mirror('good') should return a string 
holding the value gooddoog. (Hint: Make use of the reverse function).
"""

from test import testEqual

def reverse(text):
    # your code here
    
    #establish variables that will be needed
    reverse_text = ''
    string_length = -1
    
    #loop thru each string to reverse it
    for each_char in text:
        new_character = text[string_length]
        string_length = string_length - 1
        reverse_text = reverse_text + new_character
    
    return reverse_text

def mirror(text):
    # your code here
    
    mirrored_text = text + reverse(text)
    
    return mirrored_text

def main():
    user_string = str(input("Please type in the string of characters you wish to analyze."))
    
    print(mirror(user_string))
                        
if __name__ == "__main__":
    main()

testEqual(mirror('good'), 'gooddoog')
testEqual(mirror('Python'), 'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'), 'aa')

"""
#7
Write a function that implements a substitution cipher. In a substitution cipher one letter is 
substituted for another to garble the message. For example A -> Q, B -> T, C -> G etc. your 
function should take two parameters, the message you want to encrypt, and a string that represents 
the mapping of the 26 letters in the alphabet. Your function should return a string that is the 
encrypted version of the message.
"""

def encrypt(text, cipher):
    
    #define variables that will be needed
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uppercase_string = text.upper()
    encrypted_text = ''
    
    #loop thru the original message replacing original characters with the cypher characters
        
    for char in uppercase_string:
        if char == ' ':
           encrypted_text = encrypted_text + ' ' 
        else:
            position = alphabet.index(char)
            encrypted_text = encrypted_text + cipher[position]
    
    
    return encrypted_text
    
def main():
    user_string = str(input("Please type in the string of characters you wish to encrypt."))
    
    cipher = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
 
    print(encrypt(user_string, cipher))
                        
if __name__ == "__main__":
    main()

"""
#8
Write a function that decrypts the message from the previous exercise. It should also take two parameters. 
The encrypted message, and the mixed up alphabet. The function should return a string that is the same 
as the original unencrypted message.
"""

def decrypt(encrypted, cipher):
    #define the variables that will be needed
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ''
    
    #loop thru the encrypted message and replace them with the original characters
    for char in encrypted:
        if char == ' ':
            decrypted_text = decrypted_text + ' '
        else:
            position = cipher.index(char)
            decrypted_text = decrypted_text + alphabet[position]
        
    #return the result
    
    return decrypted_text
    
def encrypt(text, cipher):
    
    #define variables that will be needed
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uppercase_string = text.upper()
    encrypted_text = ''
    
    #loop thru the original message replacing original characters with the cypher characters
        
    for char in uppercase_string:
        if char == ' ':
           encrypted_text = encrypted_text + ' ' 
        else:
            position = alphabet.index(char)
            encrypted_text = encrypted_text + cipher[position]
    
    
    return encrypted_text
    
def main():
    user_string = str(input("Please type in the string of characters you wish to encrypt."))
    
    cipher = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
 
    print(user_string)
    
    encrypted = encrypt(user_string, cipher)
    
    print(encrypt(user_string, cipher))
    
    print(decrypt(encrypted, cipher))
                        
if __name__ == "__main__":
    main()

"""
#9
Write a function called rot13 that uses the Caesar cipher to encrypt a message. The Caesar cipher 
works like a substitution cipher but each character is replaced by the character 13 characters to 
“its right” in the alphabet. So for example the letter “a” becomes the letter “n”. If a letter is 
past the middle of the alphabet then the counting wraps around to the letter “a” again, so “n” becomes 
“a”, “o” becomes “b” and so on. Hint: Whenever you talk about things wrapping around its a good idea 
to think of modulo arithmetic (using the remainder operator).
"""

def rot13(message):
    #define the variables that will be needed
    uppercase_message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_message = ''
    original_position = 0
    new_position = 0

    for character in uppercase_message:
        if character == ' ':
            encrypted_message = encrypted_message + ' '   #ignore spaces in the encryption
        else:
            original_position = alphabet.index(character)   #get the original position of the character
            new_position = int(original_position) + 13   #get the new position of the character
            if new_position >= 26:
                new_position = new_position % 26
            else:
                new_position = new_position
            
            #print(new_position)
            encrypted_message = encrypted_message + alphabet[new_position]

    return encrypted_message
    
def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()
