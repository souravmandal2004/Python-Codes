# Creating the decorator function
def debug (fn):
    def wrapper (*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        krargs_value = ", ".join(f"{key}: {value}" for key, value in kwargs.items())

        print ("Printing the arguments: ")
        print (args_value)
        print (krargs_value)


        print ("Printing the name of the function: ")
        print (fn.__name__)
        return fn (*args, **kwargs)
        
    return wrapper




@debug
def greet (name, greeting="Hello"):
    print (f"{greeting} {name}")


# greet ("Mandal")