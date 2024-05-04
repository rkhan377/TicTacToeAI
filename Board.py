class Board:
    def __init__(self):
        self.boardArray = [ ['-']*3 for i in range(3)]

    def setBoard(self, letters): #sets board to a specific state for testing
        if len(letters) != 9:
            return None
        i = 0
        for row in range(3):
            for col in range(3):
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
            return "X"
        if self.checkWin('O'):
            print("O wins")
            return "O"
        for row in self.boardArray:
            if any(space == '-' for space in row):
                return "In Progress"
        print("Tie")
        return "Tie"
    
    def printBoard(self):
        for row in self.boardArray:
            print(row)


