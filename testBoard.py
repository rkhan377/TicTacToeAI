from Board import Board
from Opponent import Opponent
import random
import time





def runSim(num):
    
    times = []
    results = []
    for i in range(num):
        board = Board(4)
        bot = Opponent("X", "hard", 5)
        bot2 = Opponent("O", "hard", 5)
        turn = 1
        row = random.randint(0,board.size - 1)
        col = random.randint(0,board.size - 1)
        board.boardArray[row][col] = bot2.letter
        board.printBoard()
        
        while "In Progress" == board.isGameDone():
            t1 = time.time()
            if turn % 2 != 0: #if the turn is odd, Xs turn
                row, col = bot.playTurn(board)
                board.setLetter(bot.letter,row,col)
            else: #if the turn is even, Os turn
                row, col = bot2.playTurn(board)
                board.setLetter(bot2.letter, row, col)
            times.append(time.time() - t1)
            print("Turn "+str(turn) + " took " + str(time.time() - t1) + "s")
            board.printBoard()
            turn=turn+1
    print(times)
    average = average = sum(times)/len(times)
    print(average)
    tied = not board.checkWin("X") and not board.checkWin("O")
    results.append(1 if tied else 0)
    average = sum(results)/len(results)
    print("win/tie rate:")
    print(str(average * 100) + "%")
        
        
runSim(1)


#intialize board
board = Board(4)
#set turn counter
turn = 1
#variable used to check if we need to regenerate where to place next letter 
notPlaced = True
# loop until tie or winner


bot = Opponent("X", "hard", 2)
bot2 = Opponent("O", "hard", 2)

board.setBoard(["X", "O", "-", "O", "-", "O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
board.printBoard()
bot.heuristic4(board)

# start with a random placement
'''
row = random.randint(0,board.size - 1)
col = random.randint(0,board.size - 1)
board.boardArray[row][col] = bot2.letter
board.printBoard()
'''
'''
board.setBoard(["X", "O", "X", "O", "X", "O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"])
board.printBoard()

while "In Progress" == board.isGameDone():
    if turn % 2 != 0: #if the turn is odd, Xs turn
        while notPlaced:
            row = random.randint(0,3)
            col = random.randint(0,3)
            #row, col = bot.playTurn(board)
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
