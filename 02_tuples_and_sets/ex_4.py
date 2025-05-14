n = int(input())

info = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        info.add(number)
    else:
        info.remove(number)

if info:
    print(*info, sep="\n")
else:
    print("Parking Lot is Empty")