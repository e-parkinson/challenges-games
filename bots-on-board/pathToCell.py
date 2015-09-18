def changeCharAtPos(a, b, char, lsBoard):
    workingList = lsBoard[a]
    workingList.insert(b, char)
    popAt = b + 1
    workingList.pop(popAt)
    return lsBoard

def printBoard(lsBoard):
    for i in range(0, len(lsBoard)):
        print(*lsBoard[i], sep='')

def nextMove(a, b, x, y):
    if (not a==x) or not (b==y):
        if a < x:
            print('DOWN')
            a = a + 1
        elif a > x:
            print('UP')
            a = a - 1
        elif b < y:
            print('RIGHT')
            b = b + 1
        elif b > y:
            print('LEFT')
            b = b - 1
        else:
            print('error')
        nextMove(a, b, x, y)
    else:
        print('found')

print('Game board size n x n.\nValue of n?')
n = int(input())

lsBoard = [] #prepare rows
while len(lsBoard) < n:
    lsBoard.append([])

for i in range(0,len(lsBoard)): #prepare columns
    workingList = lsBoard[i]
    while len(workingList) < n:
        workingList.append('. ')

print('Starting position (2 integers \'row column\' space separated)?')
a, b = input().split()
a,b = int(a),int(b)
lsBoard = changeCharAtPos(a, b, '@ ', lsBoard)

print('Goal position (2 integers \'row column\' space separated)?')
x, y = input().split()
x,y = int(x),int(y)
lsBoard = changeCharAtPos(x, y, '0 ', lsBoard)

print('\nStarting state: ')
printBoard(lsBoard)

print('\nPath to goal cell: ')
nextMove(a, b, x, y)
