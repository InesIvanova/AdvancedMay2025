def boarding_passengers(capacity, *args):
    stats = {}
    total_people_to_onboard = 0
    for count, group_name in args:
        total_people_to_onboard += count
        if capacity >= count:
            if group_name not in stats:
                stats[group_name] = 0
            stats[group_name] += count
            capacity -= count
    result = "Boarding details by benefit plan:\n"

    sorted_stats = sorted(stats.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for group_name, count in sorted_stats:
        result += f"## {group_name}: {count} guests\n"

    total_onboarded = sum(stats.values())

    if total_onboarded == total_people_to_onboard:
        result += "All passengers are successfully boarded!"

    if capacity == 0 and (total_people_to_onboard > total_onboarded):
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    if capacity != 0 and (total_people_to_onboard > total_onboarded):
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))