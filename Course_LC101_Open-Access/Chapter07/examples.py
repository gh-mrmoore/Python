def a():
    b()

def b():
    c()

def c():
    d()

def d()
    try:
        # processing code
        if special_error_happened:
            raise MyError
    except MyError:
        # execute if the MyError message happened

def main()
    a()


def slices_per_person(num_people):
    num_slices = 8
    slices_per_person = num_slices / num_people
    return slices_per_person

def main():
    num_people_str = input("Number of people attending the pizza party: ")
    num_people_int = int(num_people_str)
    try:
        print("Each person gets", slices_per_person(num_people_int), "slices")
    except ZeroDivisionError:
        print("You must enter a number other than zero. Don't make me sad.")
        main()

if __name__ == "__main__":
    main()


try:
    f = open("my_file.txt", "w")
    try:
        f.write("Writing some data to the file")
    finally:
        f.close()
except IOError:
    print("Error: my_file.txt does not exist or it can't be opened for output.")


