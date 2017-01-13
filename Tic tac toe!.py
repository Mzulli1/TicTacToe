import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

##              test stalemate board
##theBoard = {'top-L': 'X', 'top-M': 'O', 'top-R': 'O',
##            'mid-L': 'O', 'mid-M': 'O', 'mid-R': 'X',
##            'low-L': 'X', 'low-M': 'X', 'low-R': 'O'}


## numpad board will be supported eventually

numpadBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

def gameValid():
    if (('X'==theBoard['top-L']==theBoard['top-M']==theBoard['top-R'])
           or('X'==theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R'])
           or('X'==theBoard['low-L']==theBoard['low-M']==theBoard['low-R'])
           or('X'==theBoard['top-L']==theBoard['mid-L']==theBoard['low-L'])
           or('X'==theBoard['top-M']==theBoard['mid-M']==theBoard['low-M'])
           or('X'==theBoard['top-R']==theBoard['mid-R']==theBoard['low-R'])
           or('X'==theBoard['top-L']==theBoard['mid-M']==theBoard['low-R'])
           or('X'==theBoard['top-R']==theBoard['mid-M']==theBoard['low-L'])):
        return 'X'
    elif (('O'==theBoard['top-L']==theBoard['top-M']==theBoard['top-R'])
           or('O'==theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R'])
           or('O'==theBoard['low-L']==theBoard['low-M']==theBoard['low-R'])
           or('O'==theBoard['top-L']==theBoard['mid-L']==theBoard['low-L'])
           or('O'==theBoard['top-M']==theBoard['mid-M']==theBoard['low-M'])
           or('O'==theBoard['top-R']==theBoard['mid-R']==theBoard['low-R'])
           or('O'==theBoard['top-L']==theBoard['mid-M']==theBoard['low-R'])
           or('O'==theBoard['top-R']==theBoard['mid-M']==theBoard['low-L'])):
        
        return 'O'

    elif ((' '!= theBoard['top-L'])
          or(' '!=theBoard['top-M'])
          or(' '!=theBoard['top-R'])
          or(' '!=theBoard['mid-L'])
          or(' '!=theBoard['mid-M'])
          or(' '!=theBoard['mid-R'])
          or(' '!=theBoard['low-L'])
          or(' '!=theBoard['low-M'])
          or(' '!=theBoard['low-R'])):
        
        return 'no one'
          

        
    else:
        return True

coinFlip = random.randint(1,2)
if coinFlip == 1:
    turn = 'X'
else:
    turn = 'O'

print('Welcome to Tic Tac Toe!')
print('The format is simple: Type the move you would like to make!')
print('specify move with top, mid, or low and L M or R separated by a "-"')
print('heres an example: top-M (remember responces are case sensitive)')
printBoard(theBoard)

while gameValid() == True:
    print('Turn for '+turn+'. Move on which space?')
    move=input()
    try:
        if theBoard[move]== ' ':
            theBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            printBoard(theBoard)
        else:
            print('That spots taken, dumbass. Try again.')

    except KeyError:
        print('Invalid responce!')
        
print(str(gameValid())+ ' wins! ')
    
        

    
        



