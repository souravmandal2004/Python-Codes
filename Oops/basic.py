#Defining a class
class Car:

    # Create a variable of class type which keeps track how many cars have been created
    total_car = 0

    # Constructor
    def __init__(self, brand, model):
        self.__brand = brand        # brand is now a private attribute
        self.__model = model
        Car.total_car += 1

    def get_brand (self):
        return self.__brand
    def fullName (self):
        print (self.__brand + " " + self.__model)

    def fuel_type (self):
        return "Pertrol or Diesel"

    # Add a static method which returns a general description of this class
    @staticmethod
    def general_description ():
        return "Cars are means of transport"

    @property
    def model (self):
        return self.__model


#Inheritance
class ElectricCar (Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type (self):
        return "Electric charge"


new_car_tesla = ElectricCar ("Tesla", "Model S", "85kWh")
print (new_car_tesla.fullName())

# Check if the new_car_tesla is an instance of Car and ElectricCar
print (isinstance (new_car_tesla, Car))
print (isinstance (new_car_tesla, ElectricCar))

# Creating an object/instance
my_car = Car ("Toyota", "Corolla")
# print (my_car.brand)
print (my_car.model)
my_car.fullName ()


# printing the fuel type
print (my_car.fuel_type())
print (new_car_tesla.fuel_type())


# Calling the static method through the class
print (Car.general_description())


# Accessing the model now
print (my_car.model)