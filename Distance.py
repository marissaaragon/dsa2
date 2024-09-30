import csv

class Distance:
    def __init__(self, distance_csv, address_csv):
        self.distances = self.load_distances(distance_csv)
        self.addresses= self.load_addresses(address_csv)

    def load_distances(self, distance_csv):
        with open(distance_csv) as distance:
            reader = csv.reader(distance)
            return list(reader)

    def load_addresses(self, address_csv):
        with open(address_csv) as address:
            reader = csv.reader(address)
            return list(reader)

    def get_address(self, address):
        for row in self.addresses:
            if address in row[2]:
                return int(row[0])

    def get_distance(self, address1, address2):
        for row in self.distances:
            if address1 in row[0] and address2 in row[1]:
                return float(row[2])
        return None




