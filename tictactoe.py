import pprint
theBoard = {'top-L': ' ', 'top-M': 'X', 'top-R': 'X', 'mid-L': 'O', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': 'X', 'low-R': ' '}
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] )
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] )

printBoard(theBoard)