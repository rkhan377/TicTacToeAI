from Board import Board
from Opponent import Opponent
import random

#intialize board
board = Board()
#set turn counter
turn = 1
#variable used to check if we need to regenerate where to place next letter 
notPlaced = True
# loop until tie or winner


bot = Opponent("X")
bot2 = Opponent("O")

# start with a random placement
row = random.randint(0,2)
col = random.randint(0,2)
board.boardArray[row][col] = bot2.letter
board.printBoard()

while "In Progress" == board.isGameDone():
    if turn % 2 != 0: #if the turn is odd, Xs turn
        while notPlaced:
            #row = random.randint(0,2)
            #col = random.randint(0,2)
            row, col = bot.playTurn(board)
            notPlaced = not board.setLetter(bot.letter,row,col)
            #print(('X',row,col))
        notPlaced = True
    else: #if the turn is even, Os turn
        while notPlaced:
            row, col = bot2.playTurn(board)
            notPlaced = not board.setLetter(bot2.letter, row, col)
            #print(('O',row,col))
        notPlaced = True
    print("Turn "+str(turn))
    board.printBoard()
    turn=turn+1
print("tied" if not board.checkWin("X") and not board.checkWin("O") else "not tied")



'''
bot = Opponent("X")

testBoard = Board()
testBoard.setBoard(["X","-","-","-","-","-","O","-","O"])
testBoard.printBoard()

turn = bot.playTurn(testBoard)
print(turn)

bot = Opponent("X")

testBoard = Board()
testBoard.setBoard(["X","O","X","O","O","X","-","-","-"])
testBoard.printBoard()

turn = bot.playTurn(testBoard)
print(turn)



bot = Opponent("X")
testBoard = Board()
testBoard.setBoard(["X","O","X","O","O","X","-","-","-"])
testBoard.printBoard()
x = bot.minimax(testBoard, "X")
print(x)
'''
