import itertools
import random
from collections import deque
import time
import sys

text = {"en": {"prompt_user": "Please choose a cell.(1-9): ",
               "choose_symbol": "Please choose your symbol (X or O): ",
               "enter_name": "Please, enter your name.(only letters and numbers allowed): ",
               "welcome_message": ("{user_name} ,welcome to Tic Tac Toe Game ! \nYour goal "
                                   "is to get three of your marks (X)"
                                   " in a row, either horizontally, vertically, or "
                                   "diagonally,\nbefore your opponent,in our "
                                   "case the computer, does.\nThe "
                                   "game is played on a 3x3 grid, numbered from 1 to 9, as shown below:"),
               "machine_turn": "\nIt's my turn",
               "player_wins": "\nCongratulations! You win in {current_move} turns",
               "machine_wins": "\nToo bad! The machine wins this time in {current_move} turns",
               "tie": "\nIt's a tie! Well played!",
               "sample_board": "| 1 | 2 | 3\n| 4 | 5 | 6\n| 7 | 8 | 9\n",
               "separator": "==========================================================",
               "cell_taken": "This cell is already taken. Please choose another one.",
               "invalid_cell": "Invalid cell number! Please choose a cell.Un integer from 1 to 9): ",
               "player_turn_prompt": "It's your turn!",
               "continue_game": "\nDo you want to play again? pres Y to continue or any key for exit: ",
               "exit_game": "Thanks for playing! Goodbye!",
               "machine_thinking": "🤔 I'm thinking",
               "result": "Result You {player_wins} : Machine {machine_wins}",
               "final_result": "Final result:\nYou {player_wins} : Machine {machine_wins}",
               "prompt_to_chose_language": "Please choose your language / Моля, "
                                           "изберете език:\n1. English\n2. Български\nEnter "
                                           "the number of your choice: ",
               "invalid_input": "Invalid choice",
               "prompt_to_chose_level": "Please choose a "
                                        "difficulty level:\n1. Easy\n2. Hard\nEnter the number of your choice: "},

        "bg": {"prompt_user": "Моля, избери клетка (от 1 до 9): ",
               "choose_symbol": "Моля, избери своя символ (X или O): ",
               "enter_name": "Моля, въведи своето име (разрешени са само букви и цифри): ",
               "welcome_message": ("{user_name}, добре дошъл в играта Морски шах!\n"
                                   "Целта ти е да подредиш три еднакви символа (X) в редица – хоризонтално,"
                                   " вертикално или по диагонал,\n"
                                   "преди противникът ти (в случая компютърът) да го направи.\n"
                                   "Играта се играе върху поле 3x3, номерирано от 1 до 9, както е показано по-долу:"),
               "machine_turn": "\nМой ред е",
               "player_wins": "\nПоздравления! Ти победи за {current_move} хода",
               "machine_wins": "\nЕ, този път спечелих аз — и то само за {current_move} хода! Готов ли си за реванш?",
               "tie": "\nРавенство! Добра игра!",
               "sample_board": "| 1 | 2 | 3\n| 4 | 5 | 6\n| 7 | 8 | 9\n",
               "separator": "=============================================================",
               "cell_taken": "Тази клетка вече е заета. Моля, избери друга.",
               "invalid_cell": "Невалиден номер на клетка! Моля, избери цяло число от 1 до 9: ",
               "player_turn_prompt": "Твой ред е!",
               "continue_game": "\nИскаш ли да играеш отново? Натисни Y за продължение или друг клавиш за изход: ",
               "exit_game": "Благодарим за участието! Довиждане!",
               "machine_thinking": "🤔 Мисля...",
               "result": "Резултат Ти: {player_wins} : Машина: {machine_wins}",
               "final_result": "Краен резултат:\nТи: {player_wins} : Машина: {machine_wins}",
               "prompt_to_chose_level": "Моля, изберете ниво на трудност:\n1. Лесно\n2. Трудно\nВъведете"
                                        " номера на избора си: ",
               "invalid_input": "Невалиден избор"}
        }

"""Game set up"""

machine_choice_for_first_three_moves = deque()
player_name, player_symbol = "", ""
machine_symbol = ""

language = "en"
level = "easy"


class InvalidUserNameError(Exception):
    pass


class InvalidSymbolError(Exception):
    pass


class InvalidUserInputError(Exception):
    pass


class CellOccupiedError(Exception):
    pass


def machine_first_three_moves_set_up():
    """
    Generates a randomized sequence of three initial move positions for the machine.

    This function is used to add unpredictability to the machine's early game behavior by
    randomly selecting a unique combination of three different cell numbers from 1 to 9
    (inclusive). These represent the cell keys (not coordinates) from which the machine
    may choose its first moves.

    Returns:
        deque[int]: A deque containing a random combination of three unique cell numbers.
                    These values will be used later for the machine's first moves and
                    to remove the corresponding entries from the empty_cells dictionary.
    """
    level_list = {"hard": [1, 3, 7, 9, 5],
                  "easy": list(range(1, 10))}

    three_cell_combination = [el for el in itertools.combinations(level_list[level], 3)]
    return deque(random.choice(three_cell_combination))


def symbol_choice(name):
    valid_symbols = ["X", "O"]
    machine_symbol_ = ''
    user_symbol = ''
    while user_symbol not in valid_symbols:
        try:
            user_symbol = get_input("choose_symbol", name=name).upper()
            if user_symbol not in valid_symbols:
                raise InvalidSymbolError
        except InvalidSymbolError:
            continue
        else:
            machine_symbol_ = "O" if user_symbol == "X" else "X"
    return user_symbol, machine_symbol_


def game_rules():
    user_name = ''
    while True:
        try:
            user_name = get_input("enter_name")
            if not user_name.isalnum():
                raise InvalidUserNameError
            break
        except InvalidUserNameError:
            continue
    show_message("separator")
    show_message("welcome_message", user_name=user_name)

    show_message("sample_board")
    u_symbol, m_symbol = symbol_choice(user_name)
    return user_name, u_symbol, m_symbol


def user_chose_language():
    valid_choice = ""
    languages = {"1": "<en", "2": "bg"}
    while not valid_choice:
        try:
            valid_choice = languages[get_input("prompt_to_chose_language")]
        except (TypeError, ValueError, KeyError):
            show_message("invalid_input")
    return valid_choice


def user_chose_level():
    valid_choice = ""
    level_dict = {"1": "easy", "2": "hard"}
    while not valid_choice:
        try:
            valid_choice = level_dict[get_input("prompt_to_chose_level")]
        except (TypeError, ValueError, KeyError):
            show_message("invalid_input")
    return valid_choice


def set_up_game():
    user_name, u_symbol, m_symbol = game_rules()
    first_three_moves = machine_first_three_moves_set_up()
    return user_name, u_symbol, m_symbol, first_three_moves


"""Front End Part"""


def thinking_dots(duration=1.5, steps=5):  # This function simulate thinking effect fo machine
    sys.stdout.write(text[language]["machine_thinking"])
    for _ in range(steps):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()


def get_input(key, **kwargs):
    return input(text[language][key].format(**kwargs))


def show_message(key, **kwargs):
    print(text[language][key].format(**kwargs))


def print_board(game_board):
    for row in game_board:
        print("+----+----+----+")
        print(f"| {'  | '.join(row)}  |")
    print("+----+----+----+")


"""
Game Algorithm Module

Functions:
- play_game: Main function that controls the game flow between user and machine.
- machine_main_logic: The computer's move logic, including attempts to win, defend, or make random moves.
- machine_attack_defend: Checks for attack or defense opportunities by analyzing rows, columns, and diagonals.
- user_moves: Handles user moves, validates input, and updates the game board.
- check_if_cell_is_empty: Checks if a given cell on the board is empty.
- rows_symbol_count: Counts symbols in rows and finds a suitable move in attack/defense mode.
- col_symbol_count: Similar to rows_symbol_count but for columns.
- count_symbols_in_diagonals: Checks diagonals for possible winning or blocking moves.
- check_for_winner: Determines if there is a winner in the game.
"""


def machine_main_logic(first_three_moves: deque, all_valid_moves: dict, matrix, current_empty_cells: dict, symbol: str,
                       user_symbol):
    """
     Handles the logic behind the machine's move in the Tic Tac Toe game.
    The logic follows this order:
    1. Attempt one of the three preselected opening moves (if any remain).
    2. Try to win by completing a row, column, or diagonal (attack).
    3. Try to block the player from winning on their next move (defend).
    4. If no attack or defense move is possible, choose a random empty cell.
    Parameters:
        first_three_moves (deque): A queue of 3 randomly chosen cell numbers to make the machine's early moves varied.
        all_valid_moves (dict): Maps cell numbers (1-9) to their corresponding (row, col) coordinates.
        matrix (list[list[str]]): The current game board.
        current_empty_cells (dict): A dict of currently available (empty) cell numbers and their coordinates.
        symbol (str): The machine's symbol ("X" or "O").
        user_symbol (str): The player's symbol ("X" or "O"), used for defensive checks.

    Returns:
        bool: True if the machine wins after this move, otherwise False.
    """
    if first_three_moves:
        cell_number = first_three_moves.popleft()
        machine_row_i, machine_coll_i = all_valid_moves[cell_number]

    else:
        cell_number = random.choice(list(current_empty_cells.keys()))
        machine_row_i, machine_coll_i = current_empty_cells[cell_number]
    attack_result = machine_attack_defend(matrix, symbol)
    if attack_result:
        machine_row_i, machine_coll_i = attack_result
        matrix[machine_row_i][machine_coll_i] = symbol
        return check_for_winner(matrix, symbol)
    defend_result = machine_attack_defend(matrix, user_symbol)
    if defend_result:
        machine_row_i, machine_coll_i = defend_result
        matrix[machine_row_i][machine_coll_i] = symbol
        return check_for_winner(matrix, symbol)
    while not check_if_cell_is_empty(all_valid_moves, matrix, cell_number):
        cell_number = random.choice(list(current_empty_cells.keys()))
        machine_row_i, machine_coll_i = current_empty_cells[cell_number]
    matrix[machine_row_i][machine_coll_i] = symbol
    del current_empty_cells[cell_number]
    return check_for_winner(matrix, symbol)


def machine_attack_defend(matrix, m_symbol):
    """
      Determines if the machine can make a winning or blocking move.
      This function checks if there is a row, column, or diagonal where the machine
      (or player, when used defensively) has two matching symbols and one empty cell.
      If such a situation is found, it returns the coordinates of the optimal move.

      The function follows this order of checks:
      1. Rows
      2. Columns
      3. Diagonals

      Parameters:
          matrix (list[list[str]]): The current game board.
          m_symbol (str): The symbol to search for ("X" or "O").
                          This is the machine's symbol for attack mode,
                          or the user's symbol for defend mode.
      Returns:
          tuple[int, int]: Coordinates (row, col) of the best move, if found.
          bool: False if no such move is possible.
      """

    empty_row_symbol_tuple = rows_symbol_count(matrix, m_symbol, machine_mode=True)
    if empty_row_symbol_tuple:
        return empty_row_symbol_tuple
    empty_coll_symbol_tuple = col_symbol_count(matrix, m_symbol, machine_mode=True)
    if empty_coll_symbol_tuple:
        return empty_coll_symbol_tuple
    empty_diagonal_symbol_tuple = count_symbols_in_diagonals(matrix, m_symbol, machine_mode=True)
    if empty_diagonal_symbol_tuple:
        return empty_diagonal_symbol_tuple
    return False


def user_moves(all_valid_moves, matrix, current_empty_cells, symbol):
    show_message("player_turn_prompt")
    user_input = 0

    while True:
        try:
            user_input = int(get_input("prompt_user"))
            if user_input not in range(1, 10):
                raise InvalidUserInputError
        except (ValueError, InvalidUserInputError):
            show_message("invalid_cell")
            continue
        try:
            if not check_if_cell_is_empty(all_valid_moves, matrix, user_input):
                raise CellOccupiedError
        except CellOccupiedError:
            show_message("cell_taken")
            continue
        break
    row_i, coll_i = all_valid_moves[user_input]
    matrix[row_i][coll_i] = symbol
    del current_empty_cells[user_input]
    return check_for_winner(matrix, symbol)


def check_if_cell_is_empty(all_valid_moves, matrix, desire_cell):
    row_i, coll_i = all_valid_moves[desire_cell]
    return matrix[row_i][coll_i] == " "


def rows_symbol_count(matrix, symbol, machine_mode=False):
    for row_idx in range(len(matrix)):
        if matrix[row_idx].count(symbol) == 3:
            return True
        if machine_mode:
            if matrix[row_idx].count(symbol) == 2 and " " in matrix[row_idx]:
                return row_idx, matrix[row_idx].index(" ")
    return False


def col_symbol_count(matrix, symbol, machine_mode=False):
    for col_idx, col in enumerate((zip(*matrix))):
        if col.count(symbol) == 3:
            return True
        if machine_mode:
            if col.count(symbol) == 2 and " " in col:
                return col.index(" "), col_idx
    return False


def count_symbols_in_diagonals(matrix, symbol, machine_mode=False):
    count_symbol_in_main_diagonal = []
    count_symbol_in_second_diagonal = []
    for idx in range(len(matrix)):
        count_symbol_in_main_diagonal.append(matrix[idx][idx])
        count_symbol_in_second_diagonal.append(matrix[idx][-idx - 1])
    if count_symbol_in_main_diagonal.count(symbol) == 3:
        return True
    if count_symbol_in_second_diagonal.count(symbol) == 3:
        return True
    if machine_mode:
        if count_symbol_in_main_diagonal.count(symbol) == 2 and " " in count_symbol_in_main_diagonal:
            return count_symbol_in_main_diagonal.index(" "), count_symbol_in_main_diagonal.index(" ")
        if count_symbol_in_second_diagonal.count(symbol) == 2 and " " in count_symbol_in_second_diagonal:
            col = len(matrix) - count_symbol_in_second_diagonal.index(" ") - 1
            return count_symbol_in_second_diagonal.index(" "), col
    return False


def check_for_winner(matrix, symbol):
    """
    Checks whether the given symbol has achieved a winning condition on the board.
    The function evaluates all possible winning combinations — rows, columns, and diagonals —
    to determine if the specified symbol ('X' or 'O') occupies an entire line.
    Args:
        matrix (list[list[str]]): The current game board represented as a 2D list.
        symbol (str): The symbol to check for a winning line (e.g., 'X' or 'O').
    Returns:
        bool: True if the symbol has a complete row, column, or diagonal; False otherwise.
    """
    return any([rows_symbol_count(matrix, symbol),
                col_symbol_count(matrix, symbol),
                count_symbols_in_diagonals(matrix, symbol)])


def play_game(board, empty_cells, combination_of_coords):
    """
    Plays a full Tic Tac Toe game between the user and the machine.

Args:
    board (list[list[str]]): A 3x3 matrix representing the game board.
    empty_cells (dict): A dictionary of currently available cells (keys: 1–9, values: coordinates).
    combination_of_coords (dict): Mapping of cell numbers to their board coordinates.

Returns:
    tuple[int, int]: (1, 0) if player wins, (0, 1) if machine wins, (0, 0) if tie.
    """
    current_move = 0
    first_move = random.choice(["machine", "player"])
    if first_move == "machine":
        current_move = 1

    user_wins = False
    machine_wins = False
    final_move = 10 if first_move == "machine" else 9

    while current_move < final_move:
        if current_move % 2 == 0:
            print_board(board)
            user_wins = user_moves(all_valid_moves=combination_of_coords, matrix=board,
                                   current_empty_cells=empty_cells, symbol=player_symbol)
            print_board(board)
            if user_wins:
                break
        else:
            show_message("machine_turn")
            thinking_dots()
            machine_wins = machine_main_logic(first_three_moves=machine_choice_for_first_three_moves,
                                              all_valid_moves=combination_of_coords, matrix=board,
                                              current_empty_cells=empty_cells, symbol=machine_symbol,
                                              user_symbol=player_symbol)

            if machine_wins:
                break

        current_move += 1

    player_win = 0
    machine_win = 0
    if user_wins:
        show_message("player_wins", current_move=current_move)
        player_win += 1
    elif machine_wins:
        show_message("machine_wins", current_move=current_move)
        machine_win += 1
    else:
        show_message("tie")
    print_board(board)
    return player_win, machine_win


def main():
    player_wins = 0
    machine_wins = 0
    combination_of_coordinates = {1: (0, 0),
                                  2: (0, 1),
                                  3: (0, 2),
                                  4: (1, 0),
                                  5: (1, 1),
                                  6: (1, 2),
                                  7: (2, 0),
                                  8: (2, 1),
                                  9: (2, 2)}

    while True:
        empty_cells = combination_of_coordinates.copy()
        board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
        p_wins, m_wins = play_game(board, empty_cells, combination_of_coordinates)
        player_wins += p_wins
        machine_wins += m_wins
        show_message("result", player_wins=player_wins, machine_wins=machine_wins)
        again = get_input("continue_game").lower()
        if again != "y":
            show_message("exit_game")
            show_message("final_result", player_wins=player_wins, machine_wins=machine_wins)
            break


if __name__ == "__main__":
    language = user_chose_language()
    level = user_chose_level()
    player_name, player_symbol, machine_symbol, machine_choice_for_first_three_moves = set_up_game()
    main()