def main ():
    
    str = input ("Enter the string: ")
    
    for i in str:
        if (str.count (i) == 1):
            print ("Character is: ", i)
            break

if __name__ == "__main__":
    main ()