GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
GENERATOR_MOD_CONSTANT = 2147483647
TEST_RUN = 5
REAL_RUN = 40000000
TEST_CURVE_BALL_RUN = 1060
CURVEBALL_RUN = 5000000

testA1 = 65
testB1 = 8921

realInputA = 116
realInputB = 299

def generatorProcess(inputNumber, factorNumber):
    output = inputNumber * factorNumber
    output = output % 2147483647
    return output


def generatorMatchNumRun(inputA, inputB, numberOfRuns):
    matchNumber = 0
    currentA = inputA
    currentB = inputB
    for i in range(0, numberOfRuns+1):
        currentA = generatorProcess(currentA, GENERATOR_A_FACTOR)
        currentB = generatorProcess(currentB, GENERATOR_B_FACTOR)

        binaryA = str(bin(currentA))[2:].zfill(16)
        binaryB = str(bin(currentB))[2:].zfill(16)

        if binaryA[len(binaryA)-16: len(binaryA)] == binaryB[len(binaryB)-16: len(binaryB)]:
            matchNumber += 1

    return matchNumber
    

#print generatorMatchNumRun(testA1, testB1, TEST_RUN)
#print generatorMatchNumRun(testA1, testB1, REAL_RUN)
#print generatorMatchNumRun(realInputA, realInputB, REAL_RUN)

def generatorMatchMultipleNumRun(inputA, inputB, numberOfRuns):
    matchNumber = 0
    currentA = inputA
    currentB = inputB
    currentAQueue = []
    currentBQueue = []
    binaryAQueue = []
    binaryBQueue = []

    for i in range(0, numberOfRuns+1):
        currentA = generatorProcess(currentA, GENERATOR_A_FACTOR)
        currentB = generatorProcess(currentB, GENERATOR_B_FACTOR)

        if currentA % 4 == 0:
            currentAQueue.append(currentA)
            binaryAQueue.append(str(bin(currentA))[2:].zfill(16))
            
        if currentB % 8 == 0:
            currentBQueue.append(currentB)
            binaryBQueue.append(str(bin(currentB))[2:].zfill(16))



    maxLen = min(5000000, min(len(binaryAQueue), len(binaryBQueue)))

    if maxLen < 5000000:
        print 'Not enough pairs'
        return maxLen

    for j in range(0, maxLen):
        binaryA = binaryAQueue[j]
        binaryB = binaryBQueue[j]
        if binaryA[len(binaryA)-16: len(binaryA)] == binaryB[len(binaryB)-16: len(binaryB)]:
            matchNumber += 1

    return matchNumber

#print generatorMatchMultipleNumRun(testA1, testB1, REAL_RUN)
print generatorMatchMultipleNumRun(realInputA, realInputB, REAL_RUN)