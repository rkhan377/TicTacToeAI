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

'''
testBoard = Board()
testBoard.setBoard(["X","O","X","O","O","X","-","-","-"])
testBoard.printBoard()
'''

class Opponent:
    def __init__(self, letter):
        self.letter = letter
        self.opponent = 'O' if letter == 'X' else 'X'
    
    def minimax(self, board, maxingPlayer): #minimax traverses the tree
    #check if terminal state
        if board.isGameDone() == self.letter:
            return 1
        elif board.isGameDone() == self.opponent:
            return -1
        elif board.isGameDone() == "Tie":
            return 0
        else:
            newBoard = board.copy()
            freeSpaces = listFreeSpaces(board)
            
            if maxingPlayer == self.letter:
                value = -1000
                #freeSpaces = listFreeSpaces(board) #possible children nodes
                outcomeValues =[] #value of each children node
                for freeSpace in freeSpaces:
                    #newBoard = Board()
                    #newBoard.boardArray=board.boardArray
                    newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                    x = self.minimax(newBoard, self.opponent)
                    outcomeValues.append(x)
                    value = max(x,value)
                return value
            else: #maxing player is O
                value = 1000
                #freeSpaces = listFreeSpaces(board) #possible children nodes
                outcomeValues = [] #value of each children node
                for freeSpace in freeSpaces:
                    #newBoard = Board()
                    #newBoard.boardArray=board.boardArray
                    newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                    x = self.minimax(newBoard, self.letter)
                    value = min(x,value)
                return value
    
    def playTurn(self, board):
        bestTile = (-1, -1)
        bestScore = -100000
        for i in range(3):
            for j in range(3):
                newBoard = board.copy()
                newBoard.boardArray[i][j] = self.letter
                score = self.minimax(newBoard, self.letter)
                if score > bestScore:
                    bestScore = score
                    bestTile = (i, j)
        return bestTile
                