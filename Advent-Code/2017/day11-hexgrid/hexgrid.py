testInput1 = 'testInput1.txt'
testInput2 = 'testinput2.txt'
testInput3 = 'testinput3.txt'
testInput4 = 'testinput4.txt'
realInput = 'input.txt'

# Look up http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
coordinateMap = {
    'nw': (-1, 0),
    'n': (-1,1),
    'ne': (0, 1),
    'se': (1, 0),
    's': (1, -1),
    'sw': (0, -1),
}

def hexGridCounter(inputFilePath):
    global coordinateMap
    currentCoordinate = [0, 0]
    maxDistance = 0

    inputFile = open(inputFilePath, 'r')
    for i in inputFile:
        directionsArray = i.split(',')

        for j in directionsArray:
            currentCoordinate[0] += coordinateMap[j][0]
            currentCoordinate[1] += coordinateMap[j][1] 

            if maxDistance < (abs(currentCoordinate[0]) + abs(currentCoordinate[1])):
                maxDistance = (abs(currentCoordinate[0]) + abs(currentCoordinate[1]))
    inputFile.close()

    distance = (abs(currentCoordinate[0]) + abs(currentCoordinate[1]))
    
    return distance, maxDistance

print hexGridCounter(testInput1)
print hexGridCounter(testInput2)
print hexGridCounter(testInput3)
print hexGridCounter(testInput4)
print hexGridCounter(realInput)