"""
Mark Klein 
Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes
04/05/25

Application using Classes to take the users input about their vehicle and then ouput the 
year, make, model, door quantity, and type of roof for the vehicle. 

"""

class Vehicle: #Created Class for vehicle

    def __init__(self, vehicle):
        self.vehicle = vehicle #Initialized variable to adopt vehicle type

class Automobile(Vehicle): #Created Class for Automobile with requested attributes
    def __init__(self, vehicle, year, make, model, doors, roof):
        super().__init__(vehicle)  

        #Initialized new attributes
        self.year = year
        self.make =make
        self.model = model
        self.doors = doors
        self.roof =  roof  

def main():
    #Get variables from user input

    print("Please input information about your vehicle: ")
    vehicle = input("What kind of vehicle do you have?: ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter number of doors (2 or 4): ")
    roof = input("Enter type of roof (solid or sun roof): ") 
    vehicle = Automobile(vehicle, year, make, model, doors, roof)  #Created object

    #print output 
    print(f"  Vehicle type: {vehicle.vehicle}")
    print(f"  Year: {vehicle.year}")
    print(f"  Make: {vehicle.make}")
    print(f"  Model: {vehicle.model}")
    print(f"  Number of doors: {vehicle.doors}")
    print(f"  Type of roof: {vehicle.roof}")


if __name__ == "__main__":
    main()
    