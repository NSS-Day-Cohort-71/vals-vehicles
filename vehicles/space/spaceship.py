from vehicles import Vehicle

class Spaceship(Vehicle):
    def __init__(self, make, model, vin, occupancy, fuel_type, fuel_efficiency,
                 fuel_capacity, manned, laser_equipped, warp_enabled, anti_gravity, orbit_distance):
        # Call the parent class's __init__ method with the required parameters
        super().__init__(make, model, vin, occupancy, fuel_type, fuel_efficiency, fuel_capacity)

        # Initialize BoxTruck-specific attributes
        self.manned = manned
        self.laser_equipped = laser_equipped
        self.warp_enabled = warp_enabled
        self.anti_gravity = anti_gravity
        self.orbit_distance = orbit_distance

    def blastoff(self):
        print(f"{self.make} {self.model} blasts off to space")

    def reenter_atmosphere(self):
        pass

    def __str__(self):
        return f"{self.make} {self.model} will orbit at {self.orbit_distance} km"