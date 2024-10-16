# Marissa Aragon - Student ID: 011423806
from datetime import datetime, time, timedelta
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
        if package is None:
            print(f"Package not found in hash table: {package_id}")
        else:
            not_delivered.append(package)
    truck.packages.clear()
    while len(not_delivered) > 0:
        next_address = 5000
        next_package = None
        for package in not_delivered:
            package_address = get_address(package.address)
            truck_address = get_address(truck.address)
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
        next_package.departure_time = truck.depart_time
        truck.time += timedelta(hours=next_address / 18)
        truck_depart_time_delta = timedelta(hours=truck.depart_time.hour, minutes=truck.depart_time.minute)
        next_package.delivery_time = truck.time + truck_depart_time_delta

        # print(f"Delivering to package {next_package.package_id}: new truck address = {truck.address}, mileage = {truck.mileage} delivery time = {next_package.delivery_time}")

# Call nearest_neighbor for trucks
nearest_neighbor(truck1)
nearest_neighbor(truck2)
nearest_neighbor(truck3)

def get_status_all(user_time):
    user_time = datetime.strptime(user_time, "%H:%M").time()
    for package_id in range(1,41):
        package = package_hash.get(package_id)
        if package.delivery_time and (datetime.combine(datetime.today(), time(0, 0)) + package.delivery_time).time() <= user_time:
            print(f"Package {package.package_id} was delivered at {(datetime.combine(datetime.today(), time(0, 0)) + package.delivery_time).time()}.")
        elif package.departure_time and package.departure_time <= user_time:
            print(f"Package {package.package_id} is en route (departed at {package.departure_time}).")
        else:
            print(f"Package {package.package_id} is at the hub (not yet departed).")

def get_status_package(package_id, user_time):
    user_time = datetime.strptime(user_time, "%H:%M").time()
    package = package_hash.get(package_id)
    if package is None:
        print(f"Package {package_id} not found.")
        return
    # Compare package delivery and departure times with the input time
    delivery_time = (datetime.combine(datetime.today(), time(0, 0)) + package.delivery_time).time() if package.delivery_time else None
    departure_time = package.departure_time if package.departure_time else None

    if delivery_time and delivery_time <= user_time:
        print(f"Package {package.package_id} was delivered at {delivery_time}.")
    elif departure_time and departure_time <= user_time:
        print(f"Package {package.package_id} is en route (departed at {departure_time}).")
    else:
        print(f"Package {package.package_id} is at the hub (not yet departed).")


class Main:
    print("Welcome to the WGU Parcel Service")
    print(f"The total mileage of the trip is {truck1.mileage+truck2.mileage+truck3.mileage}")

    while True:
        user_input = input("Type package to get package information, status for package status at specific time, or exit to exit program: ")

        if user_input == "package":
            package_id = input("Enter package id: ")
            package_id = int(package_id)
            package = package_hash.get(package_id)
            if package is None:
                print(f"Package not found. ")
            else:
                package.status = "Delivered"
                print(f"Package found: {package}")
                package.status = "At Hub"
        elif user_input == "status":
            user_choice = input("Would you like to see the status for a specific package? (y/n): ")
            if user_choice == "y":
                package_id = input("Enter package id: ")
                package_id = int(package_id)
                user_time = input("Enter the time you want to check (HH:MM format): ")
                get_status_package(package_id, user_time)
            elif user_choice == "n":
                user_time = input("Enter the time you want to check (HH:MM format): ")
                get_status_all(user_time)

        elif user_input == "exit":
            break








