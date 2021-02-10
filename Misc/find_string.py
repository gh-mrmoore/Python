def count_substring(string, search):
    counter = 0

    for i in range(0,len(string), 1):
        string_len = len(search) + i
        #print(string[i:string_len])
        if string[i:string_len] == search:
            counter = counter + 1
        else:
            counter = counter
    
    return counter

def main():
    string = "ABCDCDC"

    search = "CDC"

    print(count_substring(string, search))

#shield for running at the terminal with command-line input
if __name__ == "__main__":
    main()