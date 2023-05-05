# I SUGGEST NOT USING PICKLE BECAUSE IT MAKES THING COMPLICATED JUST USE NATIVE PYTHON, CHECK SOLVED PAST PAPERS IN THE REPOSITORY FOR EXAMPLES

import pickle

class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = ""
        self.EngineSize = 0
        self.PurchasePrice = 0


        

# wb for binary write

# Car = [CarRecord() for x in range(100)]
# CarFile = open('CarFile.txt', "wb")

# for i in range(100):
#     pickle.dump(Car[i], CarFile)

# CarFile.close()

# # rb for binary read

# CarFile = open('CarFile.txt', "rb")
# Car = []
# while True:
#     Car.append(pickle.load(CarFile))

# CarFile.close()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

ThisCar = CarRecord()
# both read and write
CarFile = open("CarFile.txt", 'rb+')
Address = hash(ThisCar.VehicleID)
CarFile.seek(Address)
pickle.dump(ThisCar, CarFile)
CarFile.close()

# exceptions

try:
    pass
except:
    pass
