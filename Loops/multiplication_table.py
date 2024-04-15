def main ():
    
    number = int (input ("Enter the number for which you want the multiplication table: "))
    
    for i in range (1, 11):
        print (number, "x", i, "=", number * i)
    
if __name__ == "__main__":
    main ()