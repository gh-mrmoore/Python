string = "Hello, WelCome to PyThoN!!"
swap_string = ""

for char in string:
    if char.isupper():
        #print("Upper case")
        swap_string = swap_string + char.lower()
    else:
        #print("lower case")
        swap_string = swap_string + char.upper()

print(swap_string)