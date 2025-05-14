n = int(input())

reservations = set()

for _ in range(n):
    res_number = input()
    reservations.add(res_number)

reservation = input()

while reservation != "END":
    reservations.remove(reservation)
    reservation = input()

print(len(reservations))

sorted_reservation = sorted(reservations)
print(*sorted_reservation, sep="\n")

