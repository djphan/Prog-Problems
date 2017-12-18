INPUT_CYCLE = 2017
INPUT_STEP = 329
INPUT_CYCLE2 = 50000000

TEST_CYCLE = 10
TEST_STEP = 3

def mapCircularBuffer(inputStep, inputCycle):
    bufferState = [0]
    currentPosition = 0
    finalIndex = 0

    for i in range(1, inputCycle + 1):
        newPosition = (currentPosition + inputStep) % len(bufferState)

        if newPosition < len(bufferState) and len(bufferState) > 1:
            if newPosition > 0:
                bufferState = bufferState[:newPosition + 1] + [i] + bufferState[newPosition + 1: len(bufferState)]
            else:
                bufferState = [bufferState[0]] + [i] + bufferState[1:len(bufferState)]

            currentPosition = newPosition + 1
        else:
            bufferState = bufferState + [i]
            currentPosition = len(bufferState) - 1

    # Part 1 Return        
    #    if (i == 2017):
    #        finalIndex = currentPosition
    #return bufferState[finalIndex + 1]

    #Part 2 Return
    return bufferState[1]

#print mapCircularBuffer(TEST_STEP, TEST_CYCLE)
#print mapCircularBuffer(TEST_STEP, INPUT_CYCLE)
#print mapCircularBuffer(INPUT_STEP, INPUT_CYCLE)
print mapCircularBuffer(INPUT_STEP, INPUT_CYCLE2)