# rows = int(input())
# nums = []
#
# for _ in range(rows):
#     row_data = [int(el) for el in input().split(", ")]
#     nums.extend(row_data)
#
# print(nums)


rows_count = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows_count)]
print(matrix)

# matrix = []
# for _ in range(rows_count):
#     row_data = [int(el) for el in input().split(', ')]
#     matrix.append(row_data)

numbers = []
for row in matrix:
    for num in row:
        numbers.append(num)
print(numbers)
flattened = [num for row in matrix for num in row]
print(flattened)
