import copy

class Board:
    def __init__(self, size):
        self.size = size
        self.boardArray = [ ['-']*size for i in range(size)]

    def setBoard(self, letters): #sets board to a specific state for testing
        if len(letters) != self.size * self.size:
            return None
        i = 0
        for row in range(self.size):
            for col in range(self.size):
                self.boardArray[row][col] = letters[i]
                i = i+1

    def setLetter(self, letter, row, col):
        if self.boardArray[row][col] == '-':
            self.boardArray[row][col] = letter
            return True
        return False

    def checkWin(self, letter):
        numAdj = 0
        #check rows
        for row in range(self.size):
            for col in range(self.size):
                if self.boardArray[row][col] == letter:
                        numAdj=numAdj+1
            if numAdj == self.size:
                return True
            else:
                numAdj = 0

        numAdj = 0
        # Check columns
        transpose = [*zip(*self.boardArray)]
        for row in range(self.size):
            for col in range(self.size):
                if transpose[row][col] == letter:
                        numAdj=numAdj+1
            if numAdj == self.size:
                return True
            else:
                numAdj = 0

        numAdj = 0
        # \ diagonal
        for i in range(self.size):
            if self.boardArray[i][i] == letter:
                numAdj = numAdj+1
        if numAdj == self.size:
            return True
        
        numAdj = 0
        # / diagonal
        for i in range(self.size):
            if self.boardArray[(self.size-1)-i][i] == letter:
                numAdj = numAdj+1
        if numAdj == self.size:
            return True

        return False
    
    def isGameDone(self):
        if self.checkWin('X'):
            #print("X wins")
            return "X"
        if self.checkWin('O'):
            #print("O wins")
            return "O"
        for row in self.boardArray:
            if any(space == '-' for space in row):
                return "In Progress"
        #print("Tie")
        return "Tie"
    
    def printBoard(self):
        for row in self.boardArray:
            print(row)
    
    def copy(self):
        copy = Board(self.size)
        for row in range(self.size):
            for col in range(self.size):
                copy.boardArray[row][col] = self.boardArray[row][col]
        return copy
    
    def listFreeSpaces(self): #return a list of tuples for each empty space on the board
        res = []
        for row in range(self.size):
            for col in range(self.size):
                if self.boardArray[row][col] == '-':
                    res.append((row,col))
        return res
