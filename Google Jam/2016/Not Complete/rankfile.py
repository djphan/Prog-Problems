import sys

numTests = input()

def collectLists( inputString ):
    outputList = []

    for i in inputString.split():
        outputList.append(int(i))

    return outputList


def rankFile(inputGrid, grid):
    trackingNumber = -1
    verticalValues = []

    for j in range (0, numBer):
        verticalValues.append([])

    for i in inputGrid:
        if int(i[0]) > trackingNumber:
            trackingNumber = int(i[0])
            grid.append(i)
            print("trigger\n")

            for k in range(0, numBer):
                verticalValues[k].append(i[k])

        else:
            continue

    return verticalValues, grid

for q in range (0, int(numTests)):
    numBer = int(input())
    loopNum = (2*numBer)-1
    trackingGrid = []
    missingList = []

    for i in range (0, loopNum):
        trackingGrid.append(collectLists(input()))

    trackingGrid = sorted(trackingGrid)

    vertOutput, horOutput = rankFile(trackingGrid, [])
    """
    for i in range (0, numBer):
        if horOutput[i] not in trackingGrid:
            missingList = horOutput[i]
            break
        elif vertOutput[i] not in trackingGrid:
            missingList = vertOutput[i]
            break

    answerString = "Case #" + str(q+1) + ":"

    for i in missingList:
        answerString += (" " + str(i))

    print (answerString)
    """
