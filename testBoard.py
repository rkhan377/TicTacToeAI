from Board import Board
import random

#intialize board
board = Board()
#set turn counter
turn = 1
#variable used to check if we need to regenerate where to place next letter 
notPlaced = True
# loop until tie or winner
while "In Progress" == board.isGameDone():
    if turn % 2 != 0: #if the turn is odd, Xs turn
        while notPlaced:
            row = random.randint(0,2)
            col = random.randint(0,2)
            notPlaced = not board.setLetter('X',row,col)
            print(('X',row,col))
        notPlaced = True
    else: #if the turn is even, Os turn
        while notPlaced:
            row = random.randint(0,2)
            col = random.randint(0,2)
            notPlaced = not board.setLetter('O',row,col)
            print(('O',row,col))
        notPlaced = True
    print("Turn "+str(turn))
    board.printBoard()
    turn=turn+1
