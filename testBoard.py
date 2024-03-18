from Board import Board
import random

#intialize board
board = Board()
#set turn counter
turn = 1
#variable used to check if we need to regenerate where to place next letter 
notPlaced = True
# loop until tie or winner
while not board.isGameDone():
    if turn % 2 != 0: #if the turn is odd, Xs turn
        while notPlaced:
            notPlaced = not board.setLetter('X',random.randint(0,2),random.randint(0,2))
        notPlaced = True
    else: #if the turn is even, Os turn
        while notPlaced:
            notPlaced = not board.setLetter('O',random.randint(0,2),random.randint(0,2))
        notPlaced = True
    print("Turn "+str(turn))
    board.printBoard()
    turn=turn+1
