def main ():
    year = int (input ("Enter the year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print ("The year you entered is leap year")
    else:
        print ("The year you entered is not leap year")
        
main ()