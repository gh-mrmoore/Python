print(type("Hello, World!"))
print(type(17))
print("Hello, World")

print(type(3.2))

print(type("17"))
print(type("3.2"))

print('This is a string.')
print("""And so is this.""")

print(3.14, int(3.14))
print(3.9999, int(3.9999))       # This doesn't round to the closest int!
print(3.0, int(3.0))
print(-3.999, int(-3.999))        # Note that the result is closer to zero

print("2345", int("2345"))        # parse a string to produce an int
print(17, int(17))                # int even works on integers
print(int("23bottles"))

message = "What's up, Doc?"
n = 17
pi = 3.14159

print(message)
print(n)
print(pi)

minutes = 645
hours = minutes / 60
print(hours)

n = input("Please enter your name: ")
print("Hello", n)

bruce = 5
print(bruce)
bruce = 7
print(bruce)

x = 6        # initialize x
print(x)
x = x + 1    # update x
print(x)

