#simple example
class Car:
    starting_speed = 45
    max_speed = 135
    make = "Dodge"
    model = "Charger"

    def ChangeSpeed(self, changeAmount):
        self.starting_speed += changeAmount


#create object instance
car1 = Car()
car2 = Car()


#accessing attributes
print(car1.starting_speed)

car1.ChangeSpeed(5)

print(car1.starting_speed)


#constructors and init method
class SUV(object):
    current_speed = 45
    max_speed = 125

    #constructor
    def __new__(cls):
        return object.__new__(cls)

    #init method
    def __init__(self, starting_speed = 55):
        self.current_speed = starting_speed
        #print(6)
    
    def __add__(self, otherVehicle):
        return SUV(self.current_speed + otherVehicle.current_speed)
    #extend/modify destroy/delete method/constructor
    #def __del__(self):
    #    print("Object", self, " has been destroyed.")

suv1 = SUV()
suv2 = SUV()


print(suv1.current_speed)


#delete/destroy objects
#del car1
#del suv1

class CrossOver(SUV):
    make = "Chevrolet"
    model = "Traverse"

cuv1 = CrossOver()

print(cuv1.make)
print(cuv1.max_speed)


#overriding methods
class Couple(Car):
    doors = 2
    max_speed = 145

    def ChangeSpeed(self, changeAmount):
        self.starting_speed -= changeAmount

coupe1 = Couple()

print(coupe1.max_speed)


#overload operator
#suv3 = suv1 + suv2
#print(suv3.current_speed)


#data hiding
class Truck:
    starting_speed = 40
    doors = 2
    __VIN = "23984lksfghpaerughp9834ghsertuigbosufb"

    def __init__(self, speed):
        self.starting_speed = speed

truck1 = Truck(45)
print("Truck 1 speed: ", truck1.starting_speed)
#print("Truck 1 VIN: ", truck1.__VIN)
print("Truck 1 VIN: ", truck1._Truck__VIN)
