# Description of the project:Idea is to create TicTacToe game. Create "numpad" logic as on keyboard. Two players should play, first player will choose
# will be 'X' or 'O', when first player decide on screen "First player will start the game" should pop up, then message "Are you ready:", user can write Y or N
# If Y, user will be asked to write on which position wants to X(or O) also table for tic-tac shoul be shown..

# I will start my code with function for table screening

from random import randint

def display_board(board):


    print(board[6] + " | " + board[7] + " | " + board[8] )
    print('----------')
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print('----------')
    print(board[0] + " | " + board[1] + " | " + board[2] )

    return board



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

    print("Player 1 will start first!")

    return player1.upper(), player2

#Function which takes in the board list object, a marker ('X' or 'O') and desired position (number 1 - 9) and assigns it to the board
def place_marker(board, marker, position):
    board[position - 1] = marker
    display_board(board)



place_marker(['', ' ', ' ','', ' ', '',' ', ' ', ' '], 'X', 6)


def win_check(board, mark):
    list_of_win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

    for a,b,c in list_of_win_positions:
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
        else:
            pass

    return False

#function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.
def choose_first():
    first_play=randint(0,1)
    print(f"First will play player {first_play + 1}")
    return str(first_play)




def space_check(board, position):
    return board[position - 1] == ' '


def full_board_check(board):
    return all(b != ' ' for b in board)

def player_choice(board):

    next_position = 'Wrong'

    while next_position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        next_position = input('Please enter your next position(1 - 9): ')
        if next_position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Sorry, please choose from 1 to 9')
        if not space_check(board, int(next_position)):
            print('Sorry, this position is not available anymore')
        else:
            return int(next_position)

