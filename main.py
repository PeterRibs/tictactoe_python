from display_board import display_board
from tictactoe import *
from win_check import win_check
from choose_first import choose_first
from player_input import player_input

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