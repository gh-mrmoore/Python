#create my functions that I want to use
def add_squares(x, y):
    z = make_square(x) + make_square(y)
    return z

def make_square(a):
    b = a * a
    return b

#create a main function to run and test at the command line
def main():
    input1 = int(input('What is the first input? '))
    input2 = int(input('What is the second input? '))

    print('result ', add_squares(input1, input2), '\n')

#shield for running at the terminal with command-line input
if __name__ == "__main__":
    main()