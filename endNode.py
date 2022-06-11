import json
import re

# from FrontEnd import tx
def jsonFile(txt):

    endInput = "ME101"
    with open('C:\RVDAR2.0\\venv\ClassToDep.json', 'r') as f:
        optimizeDestination = json.load(f)


    def tagger(str1):
        flag = False
        for i in range(len(optimizeDestination)):
            if optimizeDestination[i]["tag"] in str1:
                flag = True
                break
        if flag == True:
            endInput = optimizeDestination[i]["department"]
            return endInput
        return str1

    def getEndNode(endInput):
        with open('C:\RVDAR2.0\\venv\CampusCoordinates.json', 'r') as f:
            campusCoordinates = json.load(f)

        for counter in range(len(campusCoordinates)):
            if campusCoordinates[counter]['name'] == endInput:
                coords = campusCoordinates[counter]['co-ords']
                print(coords)
                return coords


    def getRoomCoords(endRoom):
        with open('C:\RVDAR2.0\\venv\MCA_Floor1.json', 'r') as f:
            roomCoords = json.load(f)
        for counter in range(len(roomCoords)):
            if roomCoords[counter]['name'] == endRoom:
                coords = roomCoords[counter]['co-ords']
                print(coords)
                return coords


    getEndNode(tagger(txt))

