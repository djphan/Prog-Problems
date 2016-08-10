def makeCircle(totalNum, inputString):
    kids = []
    outputValue = 0

    #Map ID to BFF
    for i in range (0, len(inputString.split())):
        kids.append((i+1, int(inputString.split()[i])))

    outputValue = kids

    return outputValue

numTests = input()

for i in range (0, int(numTests)):
    totalKids = input()
    print ("Case #" + str(i+1) +": " + str(makeCircle(totalKids, input())))
