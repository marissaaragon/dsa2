# Marissa Aragon - Student ID: 011423806
from datetime import time
from Package import *
from HashTable import *
from Truck import Truck
from Distance import  *

#Loading packages
package_hash = HashTable()
load_packages("CSV/WGU Package.csv", package_hash)

#Creating 3 trucks
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", time(8,0))
truck2 = Truck(16, 18, None, [3, 6, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0, "4001 South 700 East", time(10,20))
truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", time(9,5))







