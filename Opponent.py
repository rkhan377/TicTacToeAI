from Board import Board

def listFreeSpaces(board): #return a list of tuples for each empty space on the board
    res = []
    for row in range(3):
        for col in range(3):
            if board.boardArray[row][col] == '-':
                res.append((row,col))
    return res

def minimax(board, depth, maxingPlayer): #minimax traverses the tree
    #check if terminal state
    depth = depth+1
    if board.isGameDone() == "X":
        return 100
    elif board.isGameDone() =="O":
        return -100
    elif board.isGameDone() == "Tie":
        return 0
    else:
        if maxingPlayer =="X":
            value = -1000
            freeSpaces = listFreeSpaces(board) #possible children nodes
            outcomeValues =[] #value of each children node
            for freeSpace in freeSpaces:
                newBoard = Board()
                board.copyTo(newBoard)
                newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                x = minimax(newBoard,depth,"O") - depth
                outcomeValues.append(x)
                value = max(x,value)
            return value
        else: #maxing player is O
            value = 1000
            freeSpaces = listFreeSpaces(board) #possible children nodes
            outcomeValues =[] #value of each children node
            for freeSpace in freeSpaces:
                newBoard = Board()
                board.copyTo(newBoard)
                newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                x = minimax(newBoard,depth,"X") + depth
                outcomeValues.append(x)
                value = min(x,value)
            return value
        
def opponentMove(board, letter):
    finalMove = None
    possibleMoves = listFreeSpaces(board)
    futureMoveBoardStates = []
    for i in possibleMoves:
        newBoard = Board()
        board.copyTo(newBoard)
        newBoard.setLetter(letter,i[0],i[1])
        futureMoveBoardStates.append(newBoard)
    moveValues = []
    for i in futureMoveBoardStates:
        moveValues.append(minimax(i,0,letter))
    print(moveValues)
    if letter == "X":
        finalMove = possibleMoves[(moveValues.index(max(moveValues)))]
    else:
        finalMove = possibleMoves[(moveValues.index(min(moveValues)))]
    return finalMove


testBoard = Board()
testBoard.setBoard(["X","O","X","O","O","X","-","-","-"])
testBoard.printBoard()
#x = minimax(testBoard, "X")
print(opponentMove(testBoard,"X"))