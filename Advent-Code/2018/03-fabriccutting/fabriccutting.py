testFile = "testinput.txt"
inputFile = "input.txt"

def createFabricGrid(inputGrid, gridIndex, startingCoordinate, area):
    fabricGrid = inputGrid
    startingX = int(startingCoordinate.split(",")[0]) + 1
    startingY = int(startingCoordinate.split(",")[1]) + 1
    xLength = int(area.split("x")[0])
    yLength = int(area.split("x")[1])

    for currentX in range(startingX, startingX + xLength):
        for currentY in range(startingY, startingY + yLength):
            if (currentX, currentY) in fabricGrid:
                fabricGrid[(currentX, currentY)].append(gridIndex)
            else:
                fabricGrid[(currentX, currentY)] = [gridIndex]

    return fabricGrid


def calculateOverLappingFabric(inputFileName):
    grid = dict()
    outputOverLappingArea = 0
    file = open(inputFileName, "r")

    for gridLine in file.readlines():
        gridInformation = gridLine.split(" ")
        grid = createFabricGrid(grid, gridInformation[0], gridInformation[2].replace(":", ""), gridInformation[3])

    file.close()

    overLappingIDSet = set()
    singleIDSet = set()

    for key, value in grid.items():
        if len(value) > 1:
            outputOverLappingArea += 1

            for ID in value:
                if ID not in overLappingIDSet:
                    overLappingIDSet.add(ID)
        else:
            if value[0] not in singleIDSet:
                singleIDSet.add(value[0])

    print(outputOverLappingArea)
    print("Non Overlapping ID is " + str(singleIDSet.difference(overLappingIDSet)))

calculateOverLappingFabric(testFile)
calculateOverLappingFabric(inputFile)
