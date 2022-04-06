from geohash import *
import time

user1 = "u366x453"
user2 = "u336p322"

# threshold in meters
threshold = 25

neighborhood_layers = 4




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
    geohashList.append(geohash)     #initialen Geohash hinzufügen
    index = 0
    # if index == 1:
    #     geohashList.append(neighbors(geohash))
    #     geohashList = flattenList(geohashList)
    #     #geohashList.append(geohash)
    #     index = index+1
    #     #print("tets", geohashList)
    #   enn keine Layers dann gib initialen geohash wieder zurück
    if neighberhood_layers == 0:
        return geohashList
    #   iteriere sooft wie neighberhood_Layers gefordert werden   
    while index <= neighberhood_layers:
        index = index + 1
        tempList = []
        
        #   berechne für jeden geohash in geohahsList die Neighbours und füge sie der Teporären geohashList hinzu
        for hash in geohashList:
            tempHash = neighbors(hash)
            tempList.append(tempHash)

        #   füge tempöräre geohashListe der finalen hinzu, und "entferne" eckige Klammern in der temporären Liste
        geohashList.append(flattenList(tempList))
        
        #   wenn mehr als ein Geohash, entferne eckige klammern in finale geohashListe (die der kürzlich hinzugefügten TemporärenListe)
        if index > 0:
            geohashList = flattenList(geohashList)

        #   wenn alle Layers hinzugefügt = index hochgezählt, breche while-Schleife ab
        if index == neighberhood_layers:
            break
    # filtere alle Duplikate aus GeohashListe 
    geohashListFiltered = filterDiplicates(geohashList)

    #print("final calculated inner area of request:")
    #print(geohashListFiltered)
    #print("size of calculated geohash array:", len(geohashListFiltered))
    return geohashListFiltered


def calculateOverlap(geohashList1, geohashList2):
    overlapNumber = 0

    #überprüfe ob Länge der Listen und Länge der Geohashes gleich ist, wenn nicht gebe Error
    if len(geohashList1) == len(geohashList2) and len(geohashList1[0]) == len(geohashList2[0]):
        
        for geohash in geohashList1:
            overlapNumber += geohashList2.count(geohash)
            #print("for: ", overlapNumber)      

        overlapPercentage = int(overlapNumber/len(geohashList1) * 100)
        #print(">>> final coverage:", overlapPercentage)

        return overlapPercentage
    else:
        return -1



def isNeighbor(user1Location, user2Location, threshold):
    #for curr_user in Users.objects.all():

                #checkExpiration(curr_user)

                user1List = calculate_Area(user1, neighborhood_layers)
                user2List = calculate_Area(user2, neighborhood_layers)

                if calculateOverlap(user1List, user2List) > threshold :
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