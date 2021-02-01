x = 5

print(x)

def square_number(someNumber):
    return someNumber ** 2

print(square_number(2))

class MyClass:
    def __init__(self, nameString, intValue):
        self.nameString = nameString
        self.intValue = intValue

mc01 = MyClass("Name String", 52)

print(mc01.nameString)
print(mc01.intValue)

for x in range(10):
    print(x+1)