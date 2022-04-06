# Importing the geodesic module from the library
from geopy.distance import geodesic

import time
  
# Loading the lat-long data for Kolkata & Delhi
user1 = (22.5726, 88.3639)
user2 = (28.7041, 77.1025)

# threshold in meters
threshold = 1000

def isNeighbor(user1Location, user2Location, threshold):
    if geodesic(user1Location, user2Location).m <= threshold:
        print("user1 and user2 are neighbours")
        return True
    else:
        print("user 1 an duser2 are not neighbours")
        return False


st = time.time()
isNeighbor(user1, user2, threshold)
et = time.time()

res = et - st
res_ns = res * 1000
print('Execution time:', res_ns, 'milliseconds')
