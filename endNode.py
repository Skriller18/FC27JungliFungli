import json
import re
from frontendgui import txt

endInput = txt


with open('/Users/rahulanilal/Javascript/ClassToDep.json', 'r') as f:
    optimizeDestination = json.load(f)

def tagger(str1):
    flag = False
    for i in range(len(optimizeDestination)):
        if optimizeDestination[i]["tag"] in str1:
            flag = True
            break
    if flag == True:
        endInput = optimizeDestination[i]["department"]
        print(endInput)

tagger(endInput)


def getEndNode():
    with open('/Users/rahulanilal/Javascript/CampusCoordinates.json', 'r') as f:
        campusCoordinates = json.load(f)

    for counter in range(len(campusCoordinates)):
        if campusCoordinates[counter]['name'] == endInput:
            coords = campusCoordinates[counter]['co-ords']
            return coords
