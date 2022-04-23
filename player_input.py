def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input ('Player 1: Choose X or O: ').upper()  
    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')