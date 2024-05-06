from Board import Board
from Opponent import Opponent
import random
import time





def runSim(num):
    highestTurn = -1
    times = []
    results = []
    wins = 0
    for i in range(num):
        print("Game "+str(i+1))
        board = Board(4)
        bot = Opponent("X", "hard", 550)
        bot2 = Opponent("O", "rdm", 500)
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
            turnTime = time.time() - t1
            times.append(turnTime)
            print("Turn "+str(turn) + " took " + str(turnTime) + "s")
            if turnTime > highestTurn:
                highestTurn = turnTime
            board.printBoard()
            turn=turn+1
        
    #print(times)
    
    #print(average)
        if board.checkWin("X"):
            wins = wins +1
        #tied = not board.checkWin("X") and not board.checkWin("O")
        #results.append(1 if tied else 0)
    average = wins/num
    print("win rate:")
    print(str(average * 100) + "%")
    print("Highest Turn: "+str(highestTurn))
        
        
runSim(100)


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
#board.printBoard()
bot.heuristic4(board)

# start with a random placement
