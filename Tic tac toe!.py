import random
import time



# numpad board now supported
numpadBoard = {7: ' ', 8: ' ', 9: ' ',
               4: ' ', 5: ' ', 6: ' ',
               1: ' ', 2: ' ', 3: ' '}

# prints the board out in its current state
def printBoard(board):
    print('')
    print(board[7], board[8], board[9], sep='┃', end = '\n━╋━╋━\n')
    print(board[4], board[5], board[6], sep='┃', end = '\n━╋━╋━\n')
    print(board[1], board[2], board[3], sep='┃', end = '\n')
    print('')


# returns the winner of the game, or 'no one' if the game is tied, or True if the game is not over
def gameValid():
    matr = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for i in range(8):
        if ' '!=numpadBoard[matr[i][0]]==numpadBoard[matr[i][1]]==numpadBoard[matr[i][2]]:
            return numpadBoard[matr[i][0]]
    for i in range(1, 10):
        if numpadBoard[i] == ' ':
            return 'Valid'
    return 'no one'

#checker thingy
def check(a):
    global numpadBoard
    matr = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    matr2= [[1,2],[0,2],[0,1]]
    for i in range(8):
        for w in range(3):
            if a==numpadBoard[matr[i][matr2[w][0]]]==numpadBoard[matr[i][matr2[w][1]]] and numpadBoard[matr[i][w]]==' ':
                return matr[i][w]
            
    return 'rand'

# Where to move algorithem
def aI():
    global difficulty
    global numpadBoard
     
    if check('O')!= 'rand':
        print('skills')
        return check('O')
    elif check('X')!= 'rand':
        print ('rekt')
        return check('X')
    elif difficulty>2 and numpadBoard[5]==' ':
        return 5
    elif difficulty>3:
        courners = [1,3,7,9]
        courners2 = []
        for i in courners:
            if numpadBoard[i]==' ':
                courners2.append(i)
        if len(courners2)!= 0:
            return courners2[random.randint(0,(len(courners)-1))]
        
        else: return random.randint(1,9)
   
    else:    
        print('rand')
        return random.randint(1,9)

    #this function gets called after the game
def winBoard():
    matr = [[7,8,9], [4,5,6], [1,2,3], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    uni={0:'─', 1:'│', 2:'╱', 3:'╲'}
    unicode = {(7,8,9):uni[0], (4,5,6):uni[0], (1,2,3):uni[0], (1,4,7):uni[1], (2,5,8):uni[1], (3,6,9):uni[1], (1,5,9):uni[2], (3,5,7):uni[3]}
    
    for i in range(8):
        if ' '!=numpadBoard[matr[i][0]]==numpadBoard[matr[i][1]]==numpadBoard[matr[i][2]]:
            win=tuple(matr[i])
            break
        
    for i in win:
        numpadBoard[i] = unicode[win]
        
    printBoard(numpadBoard)
        
    
    
    
  
        
#########################################################################################################################

print('How many players?')
players = input()
if players == '1':
    print('choose diffiulty 1-4')
    difficulty = int(input())
    
print('Welcome to Tic Tac Toe!')
print('The format is simple: Type the move you would like to make!')
print('specify move with the numberpad')
printBoard(numpadBoard)
turn = 'X'
while (gameValid() == 'Valid'):
    if (players == '2') or (turn == 'X'):
        print('Turn for '+turn+'. Move on which space?')
        try:
            move=int(input())
        except ValueError:
            print('invalid responce')
    else:
       move = aI()
        
    try:
        if numpadBoard[move]== ' ': 
            numpadBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            printBoard(numpadBoard)    
        elif turn == 'X':
            print('That spots taken, dumbass. Try again.  ('+str(move)+')')

    except KeyError:
        print('Invalid responce!')

print(gameValid()+ ' wins! ')
if gameValid() != 'no one':
    winBoard()
time.sleep(100)
print('time up!')
time.sleep(10)



        

    
        




