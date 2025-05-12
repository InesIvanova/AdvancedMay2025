from collections import deque

liters = int(input())

name = input()
queue = deque()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        person_name = queue.popleft()
        liters_requested = int(command)
        if liters_requested <= liters:
            liters -= liters_requested
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    elif command.startswith("refill"):
        _, liters_to_fill = command.split(" ")
        liters_to_fill = int(liters_to_fill)
        liters += liters_to_fill
    command = input()

print(f"{liters} liters left")
