def main ():

    # Open a file
    f = open ("script.py", "r")

    # Read all the lines in the file using for loop
    for line in f:
        print (line, end="")


    # Read all the lines in the file using while loop
    while True:
        line  = f.readline()
        if (not line):
            break
        print (line, end="")

if __name__ == "__main__":
    main()