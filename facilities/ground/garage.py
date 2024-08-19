from facilities import StorageFacility
from vehicles.ground import BoxTruck

class Garage(StorageFacility):
    def __init__(self, location, capacity):
        super().__init__(location, capacity)

        self.allowed = [BoxTruck]
