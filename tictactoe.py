def place_marker (board, marker, position):
    board[position] = marker

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

