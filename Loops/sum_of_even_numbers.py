# Calculate the sum of even numbers upto a given number n

def main ():
    

    sum  = 0

    num = int (input("Enter the value of n: "))
    
    for i in range (1, num+1):
        if (i % 2 == 0):
            sum += i
    
    print ("The sum of even numbers is: ", sum)

if __name__ == "__main__":
    main ()