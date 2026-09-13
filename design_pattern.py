# # 1.Singleton

# class Singleton:
#     _instance = None #class variable
    
#     def __new__(cls):
#         if cls._instance is None:
#             print("1st obj is created")
#             cls._instance = super(Singleton, cls).__new__(cls)
            
# ob1 = Singleton()
# ob2 = Singleton()

# print(ob1 is ob2)

# 2. Factory Design System
class Car:
    def driver(self):
        return "Driving a car"
    
class Bike:
    def driver(self):
        return "Riding a bike"
    
class VehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown bike")
        
vehicle = VehicleFactory.get_vehicle("Car")
print(vehicle.driver())