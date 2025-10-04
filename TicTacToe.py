# Description of the project:Idea is to create TicTacToe game. Create "numpad" logic as on keyboard. Two players should play, first player will choose
# will be 'X' or 'O', when first player decide on screen "First player will start the game" should pop up, then message "Are you ready:", user can write Y or N
# If Y, user will be asked to write on which position wants to X(or O) also table for tic-tac shoul be shown..

# I will start my code with function for table screening

def display_board(board):


    print(board[6] + " | " + board[7] + " | " + board[8] )
    print('----------')
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print('----------')
    print(board[0] + " | " + board[1] + " | " + board[2] )

    return board

display_board(['X', ' ', ' ','O', ' ', 'X',' ', ' ', ' '])