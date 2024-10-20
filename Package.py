import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        # Initialize package with package related attributes
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departure = None
        self.delivery_time = None

    # Returns a string with package related attributes
    def __str__(self):
        return f"ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}, Delivery Deadline: {self.deadline}, Weight: {self.weight}, Delivery Time: {self.delivery_time}, Status: {self.status}"

# The load_packages function allows the csv package file to be loaded and added to the hash table
def load_packages(file, package_table):
    with open(file) as packages:
        package_data = csv.reader(packages)
        next(package_data)
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At Hub"

            p = Package(package_id, address, city, state, zip_code, deadline, weight, status)
            package_table.insert(package_id, p)