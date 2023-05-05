# inheritance
# polymorphism
# containment / aggregation

# inheritance
# a sub class can extend the parent class
# the extended class (derived class) can use the properties from the parent class without redeclaring them


# polymorphism
# when methods are redefined for derived classes
# === overloading

# containment
# a class includes instance of another class
# example: 

class Class1:
    class Student:
        pass

# class example

class Car:
    def __init__(self, n, e):
        self.__VehicleID = n
        self.__DateOfRegistration = ""
        self.__EngineSize = e
        # the two underscore mean it is private

    #  getter
    def GetVehicleID(self):
        return self.__VehicleID
    
    #  getter
    def GetEngineSize(self):
        return self.__EngineSize
    
    # setter
    def SetDateOfRegistration(self, d):
        self.__DateOfRegistration = d

    
#  instantiating a class
ThisCar = Car("ABCD", 2500)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# inheritance

class LibraryItem:
    def __init__(self,t):
        self.__Title = t

class Book(LibraryItem):
    def __init__(self, t):
        # super used to initialize the parent class
        super().__init__(t)

#  overloading // polymorphism

# just call using the base classes name
# like:  BaseClase.PrintDetails()
# in subclass:  PrintDetails()
        

#  containment

class Class1:
    class Student:
        pass
        
    class Janitor:
        pass