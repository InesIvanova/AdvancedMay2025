def calculate_next_place(current_r, current_c, direction, n, direction_mapper):
    row_movement, col_movement = direction_mapper[direction]
    next_row_index = (current_r + row_movement) % n
    next_col_index = (current_c + col_movement) % n
    return next_row_index, next_col_index


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


n = int(input())
total_nectar = 0

matrix = []
bee_position = None
bee_energy = 15
has_restored_energy = False

for i in range(n):
    row_data = list(input())
    if "B" in row_data:
        bee_position = (i, row_data.index("B"))
    matrix.append(row_data)

direction = input()
while True:
    current_row_index, current_col_index = bee_position
    next_row, next_col = calculate_next_place(current_row_index, current_col_index, direction, n, direction_mapper)
    next_element = matrix[next_row][next_col]
    matrix[current_row_index][current_col_index] = "-"
    matrix[next_row][next_col] = "B"
    bee_position = (next_row, next_col)
    bee_energy -= 1

    if next_element.isdigit():
        total_nectar += int(next_element)

    if next_element == "H":
        if total_nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if bee_energy <= 0 and total_nectar < 30:
        print(f"This is the end! Beesy ran out of energy.")
        break

    if bee_energy <= 0 and total_nectar >= 30 and not has_restored_energy:
        bee_energy = total_nectar - 30
        total_nectar = 30
        has_restored_energy = True

    if bee_energy <= 0:
        print(f"This is the end! Beesy ran out of energy.")
        break
    direction = input()

print_matrix(matrix)