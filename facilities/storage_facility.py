class StorageFacility():
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.stored_vehicles = []
        self.allowed = []

    def store_vehicle(self, vehicle):
        if vehicle.__class__ in self.allowed:
            self.stored_vehicles.append(vehicle)
        else:
            print(f"You cannot store a {vehicle.__class__} in this facility")

    def display_inventory(self):
        for vehicle in self.stored_vehicles:
            print(vehicle)
