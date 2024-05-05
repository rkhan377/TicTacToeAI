import copy

class Board:
    def __init__(self, size = 3):
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
        # Check rows
        for row in self.boardArray:
            if all(space == letter for space in row):
                return True

        # Check columns
        for col in range(self.size):
            if all(self.boardArray[row][col] == letter for row in range(self.size)):
                return True

        # Check diagonals
        if all(self.boardArray[i][i] == letter for i in range(self.size)) or all(self.boardArray[i][2-i] == letter for i in range(self.size)):
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
        cpy = Board(self.size)
        for row in range(self.size):
            for col in range(self.size):
                cpy.boardArray[row][col] = self.boardArray[row][col]
        return cpy
    
    def listFreeSpaces(self): #return a list of tuples for each empty space on the board
        res = []
        for row in range(self.size):
            for col in range(self.size):
                if self.boardArray[row][col] == '-':
                    res.append((row,col))
        return res
