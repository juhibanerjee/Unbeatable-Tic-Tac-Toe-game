#Tic Tac Toe Game with 1 player
from math import inf as infinity
from random import choice
import platform
import time
from os import system



HUMAN = -1
COMP = +1
BOARD = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

#Function to find the state and returning the score
def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

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
    return wins(state, HUMAN) or wins(state, COMP)

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

#Minimax algorithm - returns a list with [the best row, best col, best score]
def minimax(state, depth, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

#Function to clean the console once one set is printed
def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

#Function to print the board on the cosole
def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

#Function to find where AI will place its move by calling the minimax algorithm
def ai_turn(c_choice, h_choice, depth):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    if depth == 'unbeatable':
        depth = len(empty_cells(BOARD))
    if depth == 0 or game_over(BOARD):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(BOARD, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(BOARD, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)

#Function to take the move which the human will give
def human_turn(c_choice, h_choice, depth):
    if depth == 0 or game_over(BOARD):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'Human turn [{h_choice}]')
    render(BOARD, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

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
    clean()
    h_choice = ''  
    c_choice = ''  
    first = ''  
    difficulty = (str(input("Enter 'E' for EASY; 'M' for MEDIUM; 'H' for HARD")))
    if difficulty == 'E':
        ai_intelligence = 1
    elif difficulty == 'M':
        ai_intelligence = 5
    elif difficulty == 'H':
        ai_intelligence = 'unbeatable'
    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'


    # Human may starts first
    clean()
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
            ai_turn(c_choice, h_choice, ai_intelligence)
            first = ''

        human_turn(c_choice, h_choice, ai_intelligence)
        ai_turn(c_choice, h_choice, ai_intelligence)

    # Game over message
    if wins(BOARD, HUMAN):
        clean()
        print(f'Human turn [{h_choice}]')
        render(BOARD, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(BOARD, COMP):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(BOARD, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(BOARD, c_choice, h_choice)
        print('DRAW!')

    exit()