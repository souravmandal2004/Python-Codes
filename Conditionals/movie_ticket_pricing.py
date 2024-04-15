def main ():
    age = int (input("Enter your age: "))
    day = "Wednesday"
    
    if day == "Wednesday":
        if age >= 18:
            print ("Ticket price is $10 because of $2 discount")
        else:
            print ("Ticket price is $6 because of $2 discount")
    else:
        if age >= 18:
            print ("Ticket price is $12")
        else:
            print ("Ticket price is $8")

main ()