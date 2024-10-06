# Marissa Aragon - Student ID: 011423806
from datetime import time
from Package import *
from HashTable import *
from Truck import Truck
from Distance import  *

#Loading packages
package_hash = HashTable()
load_packages("CSV/WGU Package.csv", package_hash)

# Distance

distance_csv = Distance("Distance.csv", "Address.csv")
#Creating 3 trucks
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", time(8,0))
truck2 = Truck(16, 18, None, [3, 6, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", time(10,20))
truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", time(9,5))

def nearest_neighbor(truck):
    not_delivered = []
    for package_id in truck.packages:
        package = package_hash.get(package_id)
        not_delivered.append(package)
    truck.packages.clear()

    while not_delivered:
        nearest_dist = float('inf')
        nearest_package = None

        for package in not_delivered:
            package_distance = distance_csv.get_address(package.address)
            truck_distance = distance_csv.get_address(truck.address)

            dist_to_package = distance_csv.get_distance(truck_distance, package_distance)

            if dist_to_package is not None and dist_to_package < nearest_dist:
                nearest_dist = dist_to_package
                nearest_package = package

        if nearest_package:
            truck.packages.append(nearest_package.id)
            truck.mileage += nearest_dist
            truck.address = nearest_package.address

            not_delivered.remove(nearest_package)

nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)

# Start Main program











