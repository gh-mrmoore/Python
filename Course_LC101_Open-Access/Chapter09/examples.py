fruit = "banana"
baked_good = " nut bread"
print(fruit + baked_good)

#---------------------------------

print("Go" * 6)

name = "Packers"
print(name * 3)

print(name + "Go" * 3)

print((name + "Go") * 3)

#---------------------------------

word = "banana"
if word == "banana":
    print("Yes, we have bananas!")
else:
    print("Yes, we have NO bananas!")

#----------------------------------

print("apple" < "banana")

print("apple" == "Apple")
print("apple" < "Apple")

#------------------------------------

print(chr(65))
print(chr(66))

print(chr(49))
print(chr(53))

print("The character for 32 is", chr(32), "!!!")
print(ord(" "))

#----------------------------------------

school = "LaunchCode LC101"
a_character = school[3]
print(a_character)

first_char = school[0]
print(first_char)

last_char = school[-1]
print(last_char)

#-------------------------------------------

singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
print(singers[17:21])

#-------------------------------------

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)

#-------------------------------------

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***")
print(news)

#--------------------------------------

greeting = "Hello, world!"
new_greeting = 'J' + greeting[1:]
print(new_greeting)
print(greeting)            # remains unchanged

#-------------------------------------

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + name + ".  Please come to my party on Saturday!"
    print(invitation)

#--------------------------------------------

for char in "Go Spot Go":
    print(char)

#-------------------------------------------

fruit = "apple"
for index in range(len(fruit)):
    print(fruit[index])

#--------------------------------------------

fruit = "apple"

position = 0
while position < len(fruit):
    print(fruit[position])
    position = position + 1

#----------------------------------------------

def find_char(text):
    char_exists = False

    for char in "Go Spot Go":
        if char == text:
            char_exists = True

    return char_exists

print(find_char("S"))
print(find_char("f"))

#----------------------------------------------

print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

#-----------------------------------------------

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for each_char in s:
        if each_char not in vowels:
            no_vowels = no_vowels + each_char
    return no_vowels

def main():
    print(remove_vowels("compsci"))
    print(remove_vowels("aAbEefIijOopUus"))

if __name__ == "__main__":
    main()

#-------------------------------------------

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

#---------------------------------------------


