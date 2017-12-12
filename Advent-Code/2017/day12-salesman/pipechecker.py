testInput = 'testinput.txt'
realInput = 'input.txt'

# Globals
traversedPath = set()

# Generates a base Dictionary of pipe mappings
# e.g. {
#   0 : [num1, num2, num3, ... numn],
#   1 : [num1_1, num1_2, ..., num1_n],
#   ..
# }
def generateBasePipeDictionary(inputFile):
    initDict = {}
    for lines in inputFile:
        lineArray = lines.split(' ')
        dictIndex = int(lineArray[0])
        initDict[dictIndex] = []
        for i in lineArray[2:]:
            # Clean up the input of commas and new lines
            initDict[dictIndex].append(int(i.split(',')[0].split('\n')[0]))

    return initDict

# Recursive Function to Traverse Pipes
def pipeTraversal(map, root):
    global numOfPrograms
    global traversedPath
    traversedPath.add(root)
    for nodes in map[root]:
        if nodes in traversedPath:
            #print nodes
            continue
        pipeTraversal(map, nodes)

def pipeChecker(inputFilePath):
    inputFile = open(inputFilePath, 'r')
    pathMap = generateBasePipeDictionary(inputFile)
    inputFile.close()
    pipeTraversal(pathMap, 0)

    return len(traversedPath)

#print pipeChecker(testInput)
#print pipeChecker(realInput)


def pipeGroupCounter(inputFilePath):
    numOfGroups = 0
    firstIndex = 0
    global traversedPath
    inputFile = open(inputFilePath, 'r')
    pathMap = generateBasePipeDictionary(inputFile)
    keyTracker = pathMap
    inputFile.close()
    pathMapLength = len(pathMap)

    while (pathMapLength > 0):
        numOfGroups += 1
        pipeTraversal(pathMap, firstIndex)

        for nodes in traversedPath:
            if (nodes in keyTracker):
                del keyTracker[nodes]

        pathMapLength = len(keyTracker)

        if (keyTracker.keys() != []):
            firstIndex = keyTracker.keys()[0]
        
    return numOfGroups

#print pipeGroupCounter(testInput)
print pipeGroupCounter(realInput)