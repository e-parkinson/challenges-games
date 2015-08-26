'''
Input: user enters string consisting of words without spaces
Output: each word is printed on a different line.

Favours longer words (first word where there is overlap between two valid words)
'''

def checkIfReal(word):
    real = False
    file = open('words.txt', 'r')
    word = word.lower()
    for line in file:
        if word == line.strip('\n'):
            real = True
            break
    return real
def keepTestingString(userString, n):
    testString = userString[:n]
    #checkIfReal(testString)
    if checkIfReal(testString):
        print(testString)
        userString = userString[n:]
        iterateOverString(userString)
    if not checkIfReal(testString):
        if n < 1:
            print(userString)
        else:
            n = n-1
            keepTestingString(userString, n)
        
def iterateOverString(userString):
    n = len(userString)
    keepTestingString(userString, n)
    

#main method
print('Enter string: ')
userString=str(input())
iterateOverString(userString)
