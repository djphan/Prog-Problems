testInput1 = [0, 2, 7, 0]
inputList = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

def memoryBankShuffle(inputList):
    # Starting Set
    bankConfigSet = set()
    currentConfig = inputList
    numOfConfigChanges = 0
    memBankLength = len(currentConfig)
    

    while True:
        tupleConfig = tuple(currentConfig)
        if tupleConfig in bankConfigSet:
            break

        bankConfigSet.add(tupleConfig)
        maxValue = 0
        valueIndex = 0
        
        for i in range(0, memBankLength):
            if currentConfig[i] > maxValue:
                maxValue = currentConfig[i]
                valueIndex = i 

        currentConfig[valueIndex] = 0

        for i in range(1, maxValue + 1):
            nextIndex = (valueIndex + i) % memBankLength 
            currentConfig[nextIndex] += 1
            
        numOfConfigChanges += 1
        print currentConfig

    return numOfConfigChanges

# print memoryBankShuffle(testInput1)
# print memoryBankShuffle(inputList)

def memoryBankShuffle2(inputList):
    # Starting Set
    bankConfigSet = set()
    bankConfigDict = {}
    currentConfig = inputList
    numOfConfigChanges = 0
    memBankLength = len(currentConfig)
    

    while True:
        tupleConfig = tuple(currentConfig)
        if tupleConfig in bankConfigSet:
            return numOfConfigChanges - bankConfigDict[tupleConfig] 
            break
            
        bankConfigSet.add(tupleConfig)
        bankConfigDict[tupleConfig] = numOfConfigChanges
        
        maxValue = 0
        valueIndex = 0
        
        for i in range(0, memBankLength):
            if currentConfig[i] > maxValue:
                maxValue = currentConfig[i]
                valueIndex = i 

        currentConfig[valueIndex] = 0

        for i in range(1, maxValue + 1):
            nextIndex = (valueIndex + i) % memBankLength 
            currentConfig[nextIndex] += 1
            
        numOfConfigChanges += 1



#print memoryBankShuffle2(testInput1)
print memoryBankShuffle2(inputList)