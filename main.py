# Import all package members here
from vehicles.ground import BoxTruck
from vehicles.space import Spaceship
from facilities.space import SpaceStation
from facilities.ground import Garage


# Create instances of vehicles to be stored here
van = BoxTruck(
    "Ford",
    "Max 1000",
    "fy5847hgth8g3vh38tvh83tu4h",
    2,
    "Regular",
    20,
    40,
    1000,
    5700
)

millenium_falcon = Spaceship(
    "SpaceX",
    "Millenium Falcon",
    "100000000000000",
    6,
    "Plasma",
    5,
    2000,
    True,
    True,
    True,
    True,
    15
)

# Create instances of storage facilities here
deep_space_nine = SpaceStation("Milky Way", 20, False, 70000)

deep_space_nine.store_vehicle(millenium_falcon)
deep_space_nine.store_vehicle(van)

deep_space_nine.display_inventory()

uhaul_garage = Garage("Nashville", 50)
uhaul_garage.store_vehicle(van)
uhaul_garage.store_vehicle(millenium_falcon)


van.travel()
millenium_falcon.travel()


# millenium_falcon.blastoff()


# Store vehicles in facilities here




