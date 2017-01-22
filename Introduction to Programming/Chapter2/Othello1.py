'''
Created on Jan 11, 2017

@author: thom
'''
#assigment:
'''
Enter the number of white pieces on the board:
34
Enter the number of black pieces on the board:
23
The percentage of black pieces on the board is:
35.94%
The percentage of black pieces of all the pieces on the board is:
40.35%
'''

#define constants
BOARD = 64 #is number of squares on the board
PERCENT = 100

#input
white_pieces = float(int(raw_input('Enter the number of white pieces on the board: ')))
black_pieces = float(int(raw_input('Enter the number of black pieces on the board: ')))

#calculate
total_pieces = white_pieces + black_pieces
percentage_black_pieces_of_board = float((black_pieces / BOARD)* PERCENT)
percentage_black_pieces_of_all_pieces = float((black_pieces / total_pieces)*PERCENT)

#output
print 'The percentage of black pieces on the board is %.2f%%' %percentage_black_pieces_of_board
print 'The percentage of black pieces of all the pieces on the board is: %.2f%%' %percentage_black_pieces_of_all_pieces

