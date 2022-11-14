"""
David Clond
SDEV 220 M03
clond_M03_lab.py


Complete the following steps:

    Write a Python app that has the following classes:
        A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick. A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
            year
            make
            model
            doors (2 or 4)
            roof (solid or sun roof).
        Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
        The app will then output the data in an easy-to-read and understandable format, such as this:
          Vehicle type: car
          Year: 2022
          Make: Toyota
          Model: Corolla
          Number of doors: 4
          Type of roof: sun roof

"""
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof_type):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type
    def toString(self):
        return f"Vehicle type: {self.vehicle_type}\n"+\
          f"Year: {self.year}\n"+\
          f"Make: {self.make}\n"+\
          f"Model: {self.model}\n"+\
          f"Number of doors: {self.doors}\n"+\
          f"Type of roof: {self.roof_type}\n"

#my_car = Automobile("car", 2022, "Toyota", "Corolla", 4, "sun roof")
while(True):
    vehicle = input("enter 'car': ")
    if vehicle == "car":
        break
year = input("enter model year: ")
make = input("enter make: ")
model = input("enter model: ")
doors = input("enter number of doors (2 or 4): ")
roof = input("enter roof type (solid or sun roof: ")

my_car = Automobile("car", year, make, model, doors, roof)

print(my_car.toString())