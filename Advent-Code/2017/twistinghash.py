# Populate List Input for the code puzzles
def generateInput(endNum):
    outputList = []
    for i in range(0, endNum):
        outputList.append(i)

    return outputList

# Generate a list from 0 ... n for our input
testInput1 = generateInput(5)
testInputLengthList = [3, 4, 1, 5]
# Test Outputs
# 1: 2 1 0 [3] 4
# 2: 4 3 0 [1] 2
# 3: 4 [3] 0 1 2
# 4: 3 4 2 1 [0]

realInput = generateInput(256)
realInputLengthList = [106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118]

# Function to apply twist and update
def twistingHashProcessor(inputList, lengthList):
    maxLength = len(inputList)

    # Values we will be updating    
    skipValue = 0
    currentLength = 0
    currentPosition = 0
    currentList = inputList   

    for i in lengthList:
        if i <= 1:
            currentPosition = (i + skipValue + currentPosition) % maxLength
            skipValue += 1
            continue

        newPosition = i + currentPosition + skipValue

        if (newPosition >= maxLength):
            list1 = currentList[currentPosition:maxLength]
            wrappedPosition = i - len(list1)
            list2 = currentList[:wrappedPosition]
            slicedPartialList = list1 + list2
            if len(slicedPartialList) > maxLength:
                slicedPartialList = slicedPartialList[:maxLength]
            slicedPartialList.reverse()
            tempIndex = currentPosition

            for i in slicedPartialList:
                currentList[tempIndex % maxLength] =  i
                tempIndex += 1

            newPosition = wrappedPosition
            
        else:
            # If the lower and upper bound are in the array length,
            # just reverse and update in place

            currentList[currentPosition:newPosition] = currentList[currentPosition:newPosition][::-1]

        currentPosition = newPosition
        skipValue += 1

    return currentList[0]* currentList[1]
        
print twistingHashProcessor(testInput1, testInputLengthList)

# 24492 is too high
# 22052 is too high
#print twistingHashProcessor(realInput, realInputLengthList)
