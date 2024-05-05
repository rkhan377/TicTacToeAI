from Board import Board
import random

class BoardNode:
    def __init__(self):
        self.boardState = None
        self.value = None
        self.children = []

class Opponent:
    def __init__(self, letter, difficulty = "hard", limit = 100):
        self.letter = letter
        self.difficulty = difficulty
        self.limit = limit
        self.opponent = 'O' if letter == 'X' else 'X'
        
    # 4x4 heuristic
    def heuristic4(self, board):
        adjacent = []
        for i in range(board.size):
            for j in range(board.size):
                if board.boardArray[i][j] == self.letter:
                    if i - 1 >= 0 and board.boardArray[i - 1][j] == "-":
                        adjacent.append((i - 1, j))
                    if i + 1 <= board.size - 1 and board.boardArray[i + 1][j] == "-":
                        adjacent.append((i + 1, j))
                    if j - 1 >= 0 and board.boardArray[i][j - 1] == "-":
                        adjacent.append((i, j - 1))
                    if j + 1 <= board.size - 1 and board.boardArray[i][j + 1] == "-":
                        adjacent.append((i, j + 1))
        if len(adjacent) == 0:
            while True:
                row = random.randint(0, board.size - 1)
                col = random.randint(0, board.size - 1)
                if board.boardArray[row][col] == "-":
                    return (row, col)
        
        r = random.randint(0, len(adjacent) - 1)
        return adjacent[r]
                    
    
    def minimax(self, board, depth, maxingPlayer): #minimax traverses the tree
    #check if terminal state
        depth = depth + 1
        if board.isGameDone() == self.letter:
            return 100
        elif board.isGameDone() == self.opponent:
            return -100
        elif board.isGameDone() == "Tie":
            return 0
        elif depth == self.limit:
            return 0
        else:
            #newBoard = board.copy()
            freeSpaces = board.listFreeSpaces()
                
            
            if maxingPlayer == self.letter:
                value = -1000
                #freeSpaces = listFreeSpaces(board) #possible children nodes
                #outcomeValues =[] #value of each children node
                for freeSpace in freeSpaces:
                    newBoard = board.copy()
                    newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                    x = self.minimax(newBoard, depth, self.opponent) - depth
                    #outcomeValues.append(x)
                    value = max(x, value)
                return value
            else: #maxing player is O
                value = 1000
                #freeSpaces = listFreeSpaces(board) #possible children nodes
                #outcomeValues = [] #value of each children node
                for freeSpace in freeSpaces:
                    newBoard = board.copy()
                    newBoard.setLetter(maxingPlayer,freeSpace[0],freeSpace[1])
                    x = depth + self.minimax(newBoard, depth, self.letter)
                    value = min(x,value)
                return value
            
    def playTurn(self, board):
        bestTile = (-1, -1)
        bestScore = -100000
        free = board.listFreeSpaces()
        if len(free) >= 12:
            return self.heuristic4(board)
            
        for move in free:
            newBoard = board.copy()
            newBoard.setLetter(self.letter,move[0],move[1])
            score = self.minimax(newBoard, 0, self.opponent)
            if score > bestScore:
                bestScore = score
                bestTile = (move[0], move[1])
                
        row = random.randint(0, board.size - 1)
        col = random.randint(0, board.size - 1)
        prob = random.randint(0, 9)
        if self.difficulty == "easy":
            if prob <= 2:
                return bestTile
            else:
                return (row, col)
        elif self.difficulty == "med":
            if prob <= 7:
                return bestTile
            else:
                return (row, col)
        else:
            return bestTile
                
    '''
    def playTurn3(self, board):
        finalMove = None
        possibleMoves = listFreeSpaces(board)
        futureMoveBoardStates = []
        for i in possibleMoves:
            #newBoard = Board()
            newBoard = board.copy()
            newBoard.setLetter(self.letter,i[0],i[1])
            futureMoveBoardStates.append(newBoard)
        moveValues = []
        for i in futureMoveBoardStates:
            moveValues.append(self.minimax(i,0,self.opponent))
        print(moveValues)
        if self.letter == "X":
            finalMove = possibleMoves[(moveValues.index(max(moveValues)))]
        else:
            finalMove = possibleMoves[(moveValues.index(min(moveValues)))]
        return finalMove
    '''