print("Hello\n")

#Conditions aka Decision Making
x = 50
if {x == 50}:print("Equals\n")

#Loops
myString = "Hello"
for char in myString:
    print(char)

#Loop Control
thisString = "H e l l o"
for char in thisString:
    if char == " ":
        break
    else:
        print(char)

print()

newString = "H e l l o"
for char in thisString:
    if char == " ":
        continue
    else:
        print(char)

print()

varString = "He llo"
for char in varString:
    if char == " ":
        pass
        print("Pass over")
    else:
        print(char)

print()
#Numbers
#Strings
#In-Depth Lists
#In-Depth Tuples
#In-Depth Dictionaries
#Date & Time
#Functions
#Modules
import math
print(math.pi)

#File Input and Output
userInput = input("Enter some data: ")
print(userInput)

fileData = open("data.txt", "a")
#r-read, a-append, w-write, x-create
print(fileData)
print(fileData.name)
fileData.close   #closes the file from further use
fileData.write(userInput)

#Handling Exceptions
def myfunc(var1):
    assert(var1 !=0), "Zero is invalid"
    return 10 / var1

print(myfunc(2))

try:
    myFile = open("file.txt", "r")
except IOError:
    print("File does not exist")
else:
    print("Nothing to see here")