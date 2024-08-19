from vehicles import Vehicle

class BoxTruck(Vehicle):
    def __init__(self, make, model, vin, occupancy, fuel_type, fuel_efficiency, fuel_capacity, storage_capacity, load_capacity):
        # Call the parent class's __init__ method with the required parameters
        super().__init__(make, model, vin, occupancy, fuel_type, fuel_efficiency, fuel_capacity)

        # Initialize BoxTruck-specific attributes
        self.storage_capacity = storage_capacity
        self.load_capacity = load_capacity
        self.equipment = []
        self.items = []

    def load_item(self):
        pass

    def unload_item(self):
        pass

    def __str__(self):
        return f"{self.make} {self.model} with {self.storage_capacity} cubic feet of storage and VIN #{self.vin}"