from IPython.display import clear_output
import random

def display_board (board):
    clear_output()
    print(
    ' ' + board[7] + ' ' + ' | ' + board[8] + ' | ' + board[9] + '\n' +
    '-----------\n' +
    ' ' + board[4] + ' ' + ' | ' + board[5] + ' | ' + board[6] + '\n' +
    '-----------\n' +
    ' ' + board[1] + ' ' + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input ('Player 1: Choose X or O: ').upper()  
    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker (board, marker, position):
    board[position] = marker

def win_check (board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or 
      (board[6] == mark and board[5] == mark and board[4] == mark) or 
      (board[3] == mark and board[2] == mark and board[1] == mark) or 
      (board[9] == mark and board[6] == mark and board[3] == mark) or 
      (board[8] == mark and board[5] == mark and board[2] == mark) or 
      (board[7] == mark and board[4] == mark and board[1] == mark) or 
      (board[9] == mark and board[5] == mark and board[1] == mark) or 
      (board[7] == mark and board[5] == mark and board[3] == mark)) 
 
def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check (board, position):
    return board[position] == ' '

def full_board_check (board):
    for i in range (0, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input ('Choose your position (1-9): ')
    return int(position)

def replay():
    return input('Play again? "Y" or "N"').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()

    game_on = True

    while game_on:
    # Player 1
        if turn == 'Player 1':
            display_board(board)
            print ("Player 2")
            position = player_choice(board)
            place_marker(board, player1_marker, position)

        if win_check(board, player1_marker):
            display_board(board)
            print ('You WIN!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('DRAW!')
                break
            else:
                turn = "Player 2"

    # Player 2
        if turn == "Player 2":
            display_board(board)
            print ("Player 1")
            position = player_choice(board)
            place_marker(board, player2_marker, position)

        if win_check(board, player2_marker):
            display_board(board)
            print ('You WIN!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('DRAW!')
                break
            else:
                turn = "Player 1"

    if not replay():
        break