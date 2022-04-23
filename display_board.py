from IPython.display import clear_output

def display_board (board):
    clear_output()
    print(
    ' ' + board[7] + ' ' + ' | ' + board[8] + ' | ' + board[9] + '\n' +
    '-----------\n' +
    ' ' + board[4] + ' ' + ' | ' + board[5] + ' | ' + board[6] + '\n' +
    '-----------\n' +
    ' ' + board[1] + ' ' + ' | ' + board[2] + ' | ' + board[3])
