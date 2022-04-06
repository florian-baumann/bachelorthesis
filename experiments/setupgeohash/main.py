from geohash import *
import time

user1 = "u366x453"
user2 = "u336p322"

# threshold in meters
threshold = 25

# layers around user geohashes
neighborhood_layers = 2




def flattenList(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flattenList(list_of_lists[0]) + flattenList(list_of_lists[1:])
    return list_of_lists[:1] + flattenList(list_of_lists[1:])


def filterDiplicates(List):
    return list(set(List))


def calculate_Area(geohash, neighberhood_layers):
    geohashList = []
    geohashList.append(geohash)     
    index = 0
    
    if neighberhood_layers == 0:
        return geohashList

    while index <= neighberhood_layers:
        index = index + 1
        tempList = []
        
        
        for hash in geohashList:
            tempHash = neighbors(hash)
            tempList.append(tempHash)

        
        geohashList.append(flattenList(tempList))
        
       
        if index > 0:
            geohashList = flattenList(geohashList)

        
        if index == neighberhood_layers:
            break
    
    geohashListFiltered = filterDiplicates(geohashList)

    
    return geohashListFiltered


def calculateOverlap(geohashList1, geohashList2):
    overlapNumber = 0

    
    if len(geohashList1) == len(geohashList2) and len(geohashList1[0]) == len(geohashList2[0]):
        
        for geohash in geohashList1:
            overlapNumber += geohashList2.count(geohash)
            

        overlapPercentage = int(overlapNumber/len(geohashList1) * 100)
        

        return overlapPercentage
    else:
        return -1


# Method for checking if two users are considered as neighbours with a given threshold for the minimum coverage
def isNeighbor(user1Location, user2Location, threshold):
    
    user1List = calculate_Area(user1, neighborhood_layers)
    user2List = calculate_Area(user2, neighborhood_layers)

    if calculateOverlap(user1List, user2List) > threshold :
        print("user1 and user2 are neighbours")
        return True

    else:
        print("user 1 and user2 are not neighbours")
        return False

#measurig execution time
st = time.time()
isNeighbor(user1, user2, threshold)
et = time.time()

res = et - st
res_ns = res * 1000
print('Execution time:', res_ns, 'milliseconds')