from datetime import timedelta

class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, depart_time):
        # Initialize truck with attributes related to the truck
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = timedelta()

    # Returns a string with truck attributes
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                                   self.address, self.depart_time)
