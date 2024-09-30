import csv

class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, weight, status):
        self.id = id
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
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip_code,
                                                       self.deadline, self.weight, self.delivery_time,
                                                       self.status)

def load_packages(file, package_table):
    with open(file) as packages:
        package_data = csv.reader(packages)
        next(package_data)
        for package in package_data:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            weight = package[6]
            status = "At Hub"

            package = Package(id, address, city, state, zip_code, deadline, weight, status)
            package_table.insert(id, package)


