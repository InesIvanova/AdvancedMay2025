rows = int(input())

matrix = []
for _ in range(rows):
    row_data = [int(el) for el in input().split()]
    matrix.append(row_data)

diagonal_sum = 0

for row_index in range(rows):
    diagonal_sum += matrix[row_index][row_index]




print(diagonal_sum)