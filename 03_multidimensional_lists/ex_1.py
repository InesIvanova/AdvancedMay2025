row, col = [int(el) for el in input().split(", ")]

matrix = []
total_sum = 0

for _ in range(row):
    row_data = [int(el) for el in input().split(", ")]
    total_sum += sum(row_data)
    matrix.append(row_data)


print(total_sum)
print(matrix)
