# Val's Vehicles Planning

1. Create a `Vehicle` class. Will contain properties that are common to all vehicles.
2. Other classes that will be child classes of `Vehicle` to hold category-specific properties.
3. Create a `StorageFacility` class to contain common properties of all facilities.
4. Other classes that will be child classes of `StorageFacility` to hold category-specific properties.
5. Create a method on `Vehicle` class named `travel()`.
6. Create a method on `Vehicle` class named `refuel()`.
7. `Vehicle` class needs a `trips` property, which will be a list.
8. Create a `Trip` class with the following properties
   1. `start_location` (str)
   2. `end_location` (str)
   3. `distance` (int)
   4. `duration` (int)
   5. `start_date` (date)
   6. `end_date` (date)
9. Add a `store_vehicle()` method on storage facility class
10. `StorageFacility` will have a `stored_vehicles` property as a list.
11. Add `fuel_capacity` to vehicle types.
12. Add `fuel_efficiency` property to `Vehicle`.
13. Add `fuel_type` property to `Vehicle`.
14. Add `FuelType` class
    1.  `name` (str)
    2.  `cost` (float)
15. Create a `vehicles` package
16. Create a `vehicles/air` package
17. Create a `vehicles/ground` package
18. Create a `vehicles/space` package
19. Create a `vehicles/water` package
20. Create a `facilities` package
21. Create a `facilities/air` package
22. Create a `facilities/ground` package
23. Create a `facilities/space` package
24. Create a `facilities/water` package
25. Create a `fuels` package


```py
def refuel(self, amount, cost):
    # add timestamp

```