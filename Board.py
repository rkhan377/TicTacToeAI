class Board:
    def __init__(self):
        self.boardArray = [ ['-']*3 for i in range(3)]

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
        for col in range(3):
            if all(self.boardArray[row][col] == letter for row in range(3)):
                return True

        # Check diagonals
        if all(self.boardArray[i][i] == letter for i in range(3)) or all(self.boardArray[i][2-i] == letter for i in range(3)):
            return True

        return False
    
    def isGameDone(self):
        if self.checkWin('X'):
            print("X wins")
            return True
        if self.checkWin('O'):
            print("O wins")
            return True
        for row in self.boardArray:
            if any(space == '-' for space in row):
                return False
        print("Tie")
        return True
    
    def printBoard(self):
        for row in self.boardArray:
            print(row)


