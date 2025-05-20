row = int(input())

matrix = []


for i in range(row):
    row_data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row_data)

print(matrix)

# Solution on one row - not recommended
# print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for i in range(int(input()))])
