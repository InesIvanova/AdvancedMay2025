class InvalidNumberValueError(Exception):
    pass


class InvalidNumberRangeError(Exception):
    pass


class PositionAlreadyTakenError(Exception):
    pass


position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

def read_players_data() -> tuple[tuple[str, str], tuple[str, str]]:
    player1_name = input("Player one name: ")
    player2_name = input("Player two name: ")
    player1_sign = input(f"{player1_name} would you like to play with 'X' or 'O'? ").upper()

    while player1_sign not in ["X", "O"]:
        print("Invalid choice, please select 'X' or 'O'")
        player1_sign = input(f"{player1_name} would you like to play with 'X' or 'O'? ").upper()
    player2_sign = 'O' if player1_sign == "X" else 'X'
    return ((player1_name, player1_sign), (player2_name, player2_sign))


def print_board_numeration():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def print_game_board(board: list[list[str]]):
    for row in board:
        print("| " + " | ".join(row) + " |")


def check_position(position: str, board: list[list[str]]) -> tuple[int, int]:
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberValueError

    if position < 1 or position > 9:
        raise InvalidNumberRangeError

    row_index, col_index = position_mapper[position]
    if board[row_index][col_index] != ' ':
        raise PositionAlreadyTakenError
    return (row_index, col_index)


def is_row_winner(board: list[list[str]], current_sign: str) -> bool:
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False

def is_col_winner(board: list[list[str]], current_sign: str) -> bool:
    for col_index in range(len(board)):
        col_count = 0
        for row_index in range(len(board)):
            if board[row_index][col_index] == current_sign:
                col_count += 1
        if col_count == 3:
            return True
    return False


def main_diagonal(board: list[list[str]], current_sign: str) -> bool:
    count = 0
    for row_index in range(len(board)):
        if board[row_index][row_index] == current_sign:
            count += 1
    if count == 3:
        return True
    return False

def is_opposite_diagonal(board: list[list[str]], current_sign: str) -> bool:
    count = 0
    for index in range(len(board)):
        if board[index][len(board) -1 - index] == current_sign:
            count += 1
    if count == 3:
        return True
    return False


def is_diagonal_winner(board: list[list[str]], current_sign: str) -> bool:
    if main_diagonal(board, current_sign):
        return True
    if is_opposite_diagonal(board, current_sign):
        return True
    return False


def is_winner(board: list[list[str]], current_sign: str) -> bool:
    is_row = is_row_winner(board, current_sign)
    is_col = is_col_winner(board, current_sign)
    is_diagonal = is_diagonal_winner(board, current_sign)

    if is_row or is_col or is_diagonal:
        return True
    return False


board = [[' ', ' ', ' '] for _ in range(3)]

player_1_data, player_2_data = read_players_data()
print_board_numeration()
print(f"{player_1_data[0]} starts first!")

turns = 1

while True:
    current_player_name, current_player_sign = player_1_data if turns % 2 != 0 else player_2_data
    position = input(f"{current_player_name} select position between [1-9]: ")

    try:
        row_index, col_index = check_position(position, board)
    except (InvalidNumberValueError, InvalidNumberRangeError):
        print("Please enter a number between 1 and 9")
        continue
    except PositionAlreadyTakenError:
        print("Please select an empty position")
        continue
    else:
        board[row_index][col_index] = current_player_sign
        print_game_board(board)
        turns += 1

        if turns >= 5 and is_winner(board, current_player_sign):
            print(f"{current_player_name} won!")
            break

        if turns == 10:
            print(f"Draw! No winner this game!")
            break


