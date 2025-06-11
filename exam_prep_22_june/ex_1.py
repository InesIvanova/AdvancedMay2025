from collections import deque

packages = [int(el) for el in input().split()]
couriers_capacity = deque([int(el) for el in input().split()])
total_weight = 0

while packages and couriers_capacity:
    package = packages.pop()
    current_courier = couriers_capacity.popleft()

    if current_courier >= package:
        total_weight += package

        current_courier -= package*2

        if current_courier > 0:
            couriers_capacity.append(current_courier)
    else:
        total_weight += current_courier
        package -= current_courier
        packages.append(package)

print(f"Total weight: {total_weight} kg")
if not packages and not couriers_capacity:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers_capacity:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join([str(el) for el in packages])}")
elif couriers_capacity and not packages:
    print(f"Couriers are still on duty: {', '.join([str(el) for el in couriers_capacity])} but there are no more packages to deliver.")

