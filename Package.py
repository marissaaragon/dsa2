import csv

class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
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

    def __str__(self):
        return (f"ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip_code}, Delivery Deadline: {self.deadline}, Weight: {self.weight}, Delivery Time: {self.delivery_time}, Status: {self.status}")

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

    def update_status(self, current_time):
        if self.delivery_time and self.delivery_time <= current_time:
            self.status = f"Delivered at {self.delivery_time}"
        elif self.departure_time and current_time >= self.departure_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"