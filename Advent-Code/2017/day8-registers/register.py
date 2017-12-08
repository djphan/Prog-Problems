import operator
from sys import maxint

def get_operator(operator_string):
    return {
        '<' : operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '>=': operator.ge,
        'inc': operator.add,
        'dec': operator.sub
    }[operator_string]


def findMaxRegister(registerDict):
    maxValue = -maxint
    for key in registerDict:
        if registerDict[key] > maxValue:
            maxValue = registerDict[key]

    return maxValue

def registerChecker(inputFile):
    registerMap = {}
    inputFile = open(inputFile, 'r')

    for line in inputFile:
        processedLine = line.split(" ")

        # Track these registers if they don't exist in our map
        # Init state is 0
        if (not (processedLine[0] in registerMap)):
            registerMap[processedLine[0]] = 0
        if (not (processedLine[4] in registerMap)):
            registerMap[processedLine[4]] = 0 

        conditionalCheck = get_operator(processedLine[5])(registerMap[processedLine[4]], int(processedLine[6].split('/n')[0]))

        if (conditionalCheck):
            registerMap[processedLine[0]] = get_operator(processedLine[1])(registerMap[processedLine[0]], int(processedLine[2]))
        else:
            continue

    inputFile.close()

    
    return findMaxRegister(registerMap)

# print registerChecker('testinput1.txt')
# print registerChecker('input.txt')

def registerMaxChecker(inputFile):
    registerMap = {}
    maxValue = 0
    inputFile = open(inputFile, 'r')

    for line in inputFile:
        processedLine = line.split(" ")

        # Track these registers if they don't exist in our map
        # Init state is 0
        if (not (processedLine[0] in registerMap)):
            registerMap[processedLine[0]] = 0
        if (not (processedLine[4] in registerMap)):
            registerMap[processedLine[4]] = 0 

        conditionalCheck = get_operator(processedLine[5])(registerMap[processedLine[4]], int(processedLine[6].split('/n')[0]))

        if (conditionalCheck):
            registerMap[processedLine[0]] = get_operator(processedLine[1])(registerMap[processedLine[0]], int(processedLine[2]))

            if registerMap[processedLine[0]] > maxValue:
                maxValue = registerMap[processedLine[0]] 
        else:
            continue

    inputFile.close()
    
    return maxValue

print registerMaxChecker('testinput1.txt')
print registerMaxChecker('input.txt')