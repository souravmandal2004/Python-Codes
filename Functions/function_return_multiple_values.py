def main ():
    def circle_stats (radius):
        area = 3.14 * radius * radius
        circumference = 2 * 3.14 * radius
        
        return (area, circumference)

    area, circumference = circle_stats (2)
    print ("Area is: ", area)
    print ("Circumference is: ", circumference)


if __name__ == "__main__":
    main ()