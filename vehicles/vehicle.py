class Vehicle():
    def __init__(self, make, model, vin, occupancy, fuel_type, fuel_efficiency, fuel_capacity):
        self.vin = vin
        self.fuel_type = fuel_type
        self.fuel_efficiency = fuel_efficiency
        self.fuel_capacity = fuel_capacity
        self.make = make
        self.model = model
        self.occupancy

        self.trips = []

    def refuel(self, amount):
        print("Vehicle refueled")
        pass


