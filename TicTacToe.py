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


#Function that can take a player input and assign their marker as 'X' or 'O'. Use while loop for continius asking
def player_input():
    print("Welcome to Tic Tac Toe!")

    player1 = 'Wrong'
    player2 = ' '

    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1 : Do you want to play X or O? ")
        if player1.upper() != 'X' and player1.upper() != 'O':
            print("Sorry, please choose X or O")
        elif player1.upper() == 'X':
            player2 = 'O'
        elif player1.upper() == 'O':
            player2 = 'X'
        else:
            pass

    print("Player 1 will start fist!")

    return player1.upper(), player2







def place_marker(board, marker, position):
    pass

def win_check(test_board, mark):
    pass

def choose_first():
    pass

def space_check(board, position):
    pass


