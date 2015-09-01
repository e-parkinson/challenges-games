#15 minutes
'''
    Input: 2 sets ascending order sorted, separated by semi-colon.
            Comma delimited values.
    Output: Print out the ascending order sorted intersection of the two lists, one per line.
            If no intersection, print empty.
    
'''
file = open('testValues.txt', 'r')

for line in file:
    listResults = []
    listLine = line.strip('\n').split(';')
    set1 = listLine[0].split(',')
    set2 = listLine[1].split(',')
    
    boundaryIndex = len(set1)
    for n in range(0,boundaryIndex):
        currentTest = set1[n]
        if currentTest in set2:
            listResults.append(currentTest)
    print(listResults)
    del listResults
