# Part 1
# Root Node always has children
# Want to find the node that is not a child of another root
# Process Text and track all children and parents
# Find the extra one
# Ignore dangling nodes

def findRootOfChristmasTree(inputFilePath):
    inputFile = open(inputFilePath, 'r')


    roots = set()
    children = set()

    for line in inputFile:
        processedLine = line.split(' ')
        processedLineLen = len(processedLine)
        roots.add(processedLine[0])

        for i in processedLine[3:]:
            children.add(i.split('\n')[0].split(',')[0])

    # track with two sets and id the remaining set
    for i in children:
        roots.remove(i)

    inputFile.close()    
    return roots

#print findRootOfChristmasTree('day7testinput1.txt')
#print findRootOfChristmasTree('day7input.txt')

# Part 2
# Note root is known
# My puzzle uses: hlhomy for day 7 input
# For test input use tknk
def determineImmediateBranchSum(numberMap, treeMap, root):
    # Start with base
    outputSum = numberMap[root]

    #Sum all children from the root node
    if (treeMap[root] != set()):
        for i in treeMap[root]:
            outputSum += numberMap[i]

    return outputSum


# Note only one of the siblings should be different from the rest
def traverseTree(numberMap, treeMap, root):

    pass

def findRootOfChristmasTree2(inputFilePath):
    inputFile = open(inputFilePath, 'r')
    numMapping = {}
    treeMapping = {}
    intermediateDict = {}

    for line in inputFile:
        processedLine = line.split(' ')
        processedLineLen = len(processedLine)
        processedNumber = int(processedLine[1].split('(')[1].split(')')[0])
        numMapping[processedLine[0]] = processedNumber
        children = set()

        for i in processedLine[3:]:
            children.add(i.split('\n')[0].split(',')[0])

        if children != set():
            treeMapping[processedLine[0]] = children


    return treeMapping
    for key, value in treeMapping.items():
        processingList = []
        for strings in value:
            processingList.append(numMapping[strings])
        intermediateDict[key] = [sum(processingList) + numMapping[key], processingList, numMapping[key]]

    #return intermediateDict


print findRootOfChristmasTree2('day7testinput1.txt')
# print findRootOfChristmasTree2('day7input.txt')



