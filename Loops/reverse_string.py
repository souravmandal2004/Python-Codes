def main ():
    
    str = input ("Enter the string: ")
    reversed_string = ""

    
    for char in str:
        reversed_string = char + reversed_string
    
    print (reversed_string)

if __name__ == "__main__":
    main ()