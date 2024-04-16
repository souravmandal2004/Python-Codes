def main ():
    
    # Factorial of a numner
    def factorial (num):
        if num == 1:
            return 1
        else: 
            return num * factorial (num - 1)
        
    print (factorial (5))

if __name__ == "__main__":
    main ()