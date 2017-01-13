import random

##              test stalemate board
##theBoard = {'top-L': 'X', 'top-M': 'O', 'top-R': 'O',
##            'mid-L': 'O', 'mid-M': 'O', 'mid-R': 'X',
##            'low-L': 'X', 'low-M': 'X', 'low-R': 'O'}


# numpad board now supported
numpadBoard = {7: ' ', 8: ' ', 9: ' ',
               4: ' ', 5: ' ', 6: ' ',
               1: ' ', 2: ' ', 3: ' '}

# prints the board out in its current state
def printBoard(board):
    print(board[7], board[8], board[9], sep='|', end = '\n-+-+-\n')
    print(board[4], board[5], board[6], sep='|', end = '\n-+-+-\n')
    print(board[1], board[2], board[3], sep='|')


# returns the winner of the game, or 'no one' if the game is tied, or True if the game is not over
def gameValid():
    matr = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for i in range(8):
        if ' '!=numpadBoard[matr[i][0]]==numpadBoard[matr[i][1]]==numpadBoard[matr[i][2]]:
            return numpadBoard[matr[i][0]]
    for i in range(1, 10):
        if numpadBoard[i] == ' ':
            return True
    return 'no one'

coinFlip = random.randint(1,2)
if coinFlip == 1:
    turn = 'X'
else:
    turn = 'O'

print('Welcome to Tic Tac Toe!')
print('The format is simple: Type the move you would like to make!')
print('specify move with top, mid, or low and L M or R separated by a "-"')
print('heres an example: top-M (remember responces are case sensitive)')
printBoard(numpadBoard)

while gameValid() == True:
    print('Turn for '+turn+'. Move on which space?')
    move=int(input())
    try:
        if numpadBoard[move]== ' ':
            numpadBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            printBoard(numpadBoard)
        else:
            print('That spots taken, dumbass. Try again.')

    except KeyError:
        print('Invalid responce!')
        
print(gameValid()+ ' wins! ')
    
        

    
        



