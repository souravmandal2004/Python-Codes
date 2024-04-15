def main ():

    number = int (input ("Enter the number: "))
    
    isPrime = True

    if (number > 1):
        for i in range (2, number):
            if (number % i) == 0:
                isPrime = False
                break
    
    if (isPrime):
        print ("The number is prime")

    else:
        print ("The number is not prime")

if __name__ == "__main__":
    main ()