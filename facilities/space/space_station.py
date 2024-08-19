from facilities import StorageFacility
from vehicles.space import Spaceship

class SpaceStation(StorageFacility):
    def __init__(self, location, capacity, terrestrial, tractor_beam_voltage):
        super().__init__(location, capacity)

        self.terrestrial = terrestrial
        self.tractor_beam_voltage = tractor_beam_voltage
        self.allowed = [Spaceship]
