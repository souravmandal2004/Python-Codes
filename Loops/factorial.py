def main ():
    
    number = int (input ("Enter the number for which you want factorial: "))

    factorial = 1
    i = 1

    while i <= number:
        factorial *= i
        i += 1
    
    print (f"The factorial of {number} is: {factorial}")

if __name__ == "__main__":
    main ()