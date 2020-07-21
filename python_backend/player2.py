#Tic Tac Toe Game with 2 players
from os import system
import platform
import random


PLAYER1 = -1
PLAYER2 = +1
BOARD = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

#Function that stores all the winning possibilities
def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

#Function to see whether anybody has won
def game_over(state):
    print(wins(state,PLAYER1))
    return wins(state, PLAYER1) or wins(state, PLAYER2)

#Function that returns the empty cells - returning a list of empty cells
def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

#Function to check whether a move is a valid move
def valid_move(x, y):
    if [x, y] in empty_cells(BOARD):
        return True
    else:
        return False

#Function to set the move only if that move is a valid move
def set_move(x, y, player):
    if valid_move(x, y):
        BOARD[x][y] = player
        return True
    else:
        return False

#Function to clean the console once one set is printed
def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


#Function to print the board on the cosole
def render(state, player2_choice, player1_choice):
    """
    Print the board on console
    :param state: current state of the board
    """
    print("*******")
    print(player1_choice, player2_choice)
    print("*******")
  
    chars = {
        -1: player1_choice,
        +1: player2_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

#Function to check the human move
def place_move(player2_choice, player1_choice, player):
    if game_over(BOARD):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    # clean()
    print(f'Human turn [{player1_choice}]')
    render(BOARD, player2_choice, player1_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], player)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


#The main function which calls the other functions
def main():
    player1_choice = ''  
    player2_choice = '' 
    first = ''  

    while player1_choice != 'O' and player1_choice != 'X':
        try:
            print('')
            player1_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    # Setting computer's choice
    if player1_choice == 'X':
        player2_choice = 'O'
    else:
        player2_choice = 'X'
    # Human1 may start first
    # clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(BOARD)) > 0 and not game_over(BOARD):
        if first == 'N':
            place_move(player2_choice, player1_choice, PLAYER2)
            first = ''

        place_move(player2_choice, player1_choice, PLAYER1)
        place_move(player2_choice, player1_choice, PLAYER2)

    # Game over message
    if wins(BOARD, PLAYER1):
        # clean()
        print(f'Human turn [{player1_choice}]')
        render(BOARD, player2_choice, player1_choice)
        print('YOU WIN!')
    elif wins(BOARD, PLAYER2):
        # clean()
        print(f'Computer turn [{player2_choice}]')
        render(BOARD, player2_choice, player1_choice)
        print('YOU LOSE!')
    else:
        # clean()
        render(BOARD, player2_choice, player1_choice)
        print('DRAW!')

    exit()