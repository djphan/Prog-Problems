
# Input File Names
testInput = 'testinput.txt'
realInput = 'input.txt'

def setupFirewallStartState(inputFilePath, endNum):
    firewallState = {}

    # Setup Inital Values
    for i in range(0, endNum + 1):
        firewallState[i] = 0

    inputFile = open(inputFilePath, 'r')
    for line in inputFile:
        keyValue = int(line.split(' ')[0].split(':')[0])
        value = int(line.split(' ')[1].split('\n')[0])
        if (keyValue in firewallState):
            firewallState[keyValue] = value
        else:
            print 'You should never get here so print out the key and value'
            print keyValue
            print value
            print firewallState 

    inputFile.close()
    return firewallState


def traverseFireWalls(inputFilePath, endNum):
    severityNumber = 0
    firewallState = setupFirewallStartState(inputFilePath, endNum)

    for i in range (0, endNum+1):
        if firewallState[i] == 0:
            continue

        if (i % firewallState[i] == 0):
            severityNumber += (i * firewallState[i])
            print severityNumber
            


    return severityNumber


print traverseFireWalls(testInput,6)

