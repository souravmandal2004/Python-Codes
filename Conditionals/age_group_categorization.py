def main ():
    age = int (input ("Enter the age: "))

    if age < 13:
        print ("You are a Child")
    elif age < 19 and age >= 13:
        print ("You are a teenager") 
    elif age <= 59 and age >= 20:
        print ("You are an adult")
    else:
        print ("You are senior")

main ()