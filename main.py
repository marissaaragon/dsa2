# Marissa Aragon - Student ID: 011423806
from datetime import time
from Package import *
from HashTable import *
from Truck import Truck

#Loading packages
package_hash = HashTable()
load_packages("CSV/WGU Package.csv", package_hash)

# Reading csv files

with open('CSV/Distance.csv') as file:
    distance_csv = csv.reader(file)
    distance_csv = list(distance_csv)

with open('CSV/Address.csv') as file:
    address_csv = csv.reader(file)
    address_csv = list(address_csv)

def get_address(address):
    for row in address_csv:
        if address in row[2]:
            return int(row[0])
    print(f"Address not found: {address}")
    return None

def get_distance(address1, address2):
    if address1 is None or address2 is None:
        return float('inf')
    distance = distance_csv[address1][address2]
    if distance == '':
        distance = distance_csv[address2][address1]

    return float(distance)

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

    while len(not_delivered) > 0:
        next_address = 5000
        next_package = None

        for package in not_delivered:
            package_address = get_address(package.address)
            truck_address = get_address(truck.address)
            print(f"Package ID: {package.package_id}, Package Address: {package_address}, Truck Address: {truck_address}")
            if package_address is None:
                print(f"Package address not found: {package.address}")
            if truck_address is None:
                print(f"Truck address not found: {truck.address}")
            if package_address is not None and truck_address is not None:
                distance = get_distance(truck_address, package_address)
                if distance <= next_address:
                    next_address = distance
                    next_package = package
        if next_package is None:
            break
        truck.packages.append(next_package.package_id)
        not_delivered.remove(next_package)
        truck.mileage += next_address
        truck.address = next_package.address
        print(f"Delivering to package {next_package.package_id}: new truck address = {truck.address}, mileage = {truck.mileage}")

nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)









