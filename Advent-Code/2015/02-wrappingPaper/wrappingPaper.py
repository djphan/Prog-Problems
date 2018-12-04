testInput00 = "00testfile_01.txt"
testInput01 = "01testfile_01.txt"
inputFile = "inputfile.txt"

def calculateBoxArea(inputDimensions):
    totalArea = 0
    boxSides = inputDimensions.split("x")

    for sideIndex in range(0, len(boxSides)):
        if (sideIndex == len(boxSides) - 1):
            totalArea += 2 * (int(boxSides[sideIndex]) * int(boxSides[0]))
        else: 
            totalArea += 2 * (int(boxSides[sideIndex]) * int(boxSides[sideIndex + 1]))

    return totalArea

def determineSmallestArea(inputDimensions):
    boxAreaSet = set()
    boxSides = inputDimensions.split("x")

    for sideIndex in range(0, len(boxSides)):
        if (sideIndex == len(boxSides) - 1):
            boxAreaSet.add((int(boxSides[sideIndex]) * int(boxSides[0])))
        else:
            boxAreaSet.add((int(boxSides[sideIndex]) * int(boxSides[sideIndex + 1])))
    return min(boxAreaSet)

def calculateTotalWrappingPaper(inputFile):
    totalOutput = 0
    file = open(inputFile, "r")

    for dimensons in file.readlines():
        totalOutput += calculateBoxArea(dimensons) + determineSmallestArea(dimensons)

    file.close()

    print totalOutput

#calculateTotalWrappingPaper(testInput00)
#calculateTotalWrappingPaper(testInput01)
#calculateTotalWrappingPaper(inputFile)

def calculateSmallestPerimeter(inputDimensions):
    boxAreaSet = set()
    boxSides = inputDimensions.split("x")

    for sideIndex in range(0, len(boxSides)):
        if (sideIndex == len(boxSides) - 1):
            boxAreaSet.add(2*(int(boxSides[sideIndex]) + int(boxSides[0])))
        else:
            boxAreaSet.add(2*(int(boxSides[sideIndex]) + int(boxSides[sideIndex + 1])))
    return min(boxAreaSet)

def calculateBow(inputDimensions):
    outputVolume = 1
    boxSides = inputDimensions.split("x")

    for side in boxSides:
        outputVolume *= int(side)

    return outputVolume

def calculateTotalRibbon(inputFile):
    totalOutput = 0
    file = open(inputFile, "r")

    for dimensons in file.readlines():
        totalOutput += calculateSmallestPerimeter(dimensons) + calculateBow(dimensons)

    file.close()

    print totalOutput

calculateTotalRibbon(testInput00)
calculateTotalRibbon(testInput01)
calculateTotalRibbon(inputFile)