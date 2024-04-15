# Given a list of numbers count how many numbers are positive

def main ():

    count = 0
    numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
    
    for num in numbers:
        if (num > 0):
            count += 1
    
    print ("Total positive numbers in the list are: ", count)
    
if __name__ == "__main__":
    main ()