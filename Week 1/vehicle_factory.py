class Car:
    def drive(self):
        print("Driving a car")
class Bike:
    def drive(self):
        print("Driving a bike")
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
factory = VehicleFactory()
vehicle = factory.create_vehicle("car")
vehicle.drive()