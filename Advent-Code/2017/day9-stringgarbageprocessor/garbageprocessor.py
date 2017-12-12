def stringCounter(inputFilePath):
    returnNum = 0
    depth = 0

    inputFile = open(inputFilePath, 'r')
    for line in inputFile:
        cancelFlag = False
        garbageFlag = False

        for i in line:
            # Rules
            # Cancel > ! > '<>' > '{}'
            
            if cancelFlag:
                cancelFlag = False
                continue

            if i == '!':
                cancelFlag = True
                continue

            if i == '>':
                garbageFlag = False
                continue

            if garbageFlag:
                continue

            if i == '<':
                garbageFlag = True
                continue

            if i == '{':
                depth += 1
                continue

            if i == '}':
                returnNum += depth
                depth -= 1
                continue

    inputFile.close()

    return returnNum

#print stringCounter('testinput1.txt')
#print stringCounter('testinput2.txt')
#print stringCounter('testinput3.txt')
#print stringCounter('testinput4.txt')
#print stringCounter('testinput5.txt')
#print stringCounter('testinput6.txt')
#print stringCounter('testinput7.txt')
#print stringCounter('testinput8.txt')
#print stringCounter('input.txt')


# Count only # of garbs
def stringGarbCounter(inputFilePath):
    returnNum = 0
    depth = 0

    inputFile = open(inputFilePath, 'r')
    for line in inputFile:
        cancelFlag = False
        garbageFlag = False

        for i in line:
            # Ignore < > ! { }
            if cancelFlag:
                cancelFlag = False
                continue

            if i == '!':
                cancelFlag = True
                continue

            if i == '>':
                garbageFlag = False
                continue

            # Just count the number of iterations here
            if garbageFlag:
                returnNum += 1
                continue

            if i == '<':
                garbageFlag = True
                continue

            if i == '{':
                continue

            if i == '}':
                continue

    inputFile.close()

    return returnNum

print stringGarbCounter('test1input1.txt')
print stringGarbCounter('input.txt')