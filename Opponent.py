from Board import Board
class BoardNode:
    def __init__(self):
        self.boardState = None
        self.value = None
        self.children = []



def listFreeSpaces(board): #return a list of tuples for each empty space on the board
    res = []
    for row in range(3):
        for col in range(3):
            if board.boardArray[row][col] == '-':
                res.append((row,col))
    return res

def minimax(board, maxingPlayer): #minimax traverses the tree
    #check if terminal state
    if board.isGameDone() == "X":
        return 1
    elif board.isGameDone() =="O":
        return -1
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
                x = minimax(newBoard,"O")
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
                value = min(minimax(newBoard,"X"),value)
            return value

testBoard = Board()
testBoard.setBoard(["X","O","X","O","O","X","-","-","-"])
testBoard.printBoard()
x = minimax(testBoard, "X")
print(x)