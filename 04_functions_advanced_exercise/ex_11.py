def math_operations(*args, **kwargs):
    firsts = []
    seconds = []
    thirds = []
    fourths = []
    for index in range(len(args)):
        if index % 4 == 0:
            firsts.append(args[index])
        elif index % 4 == 1:
            seconds.append(args[index])
        elif index % 4 == 2:
            thirds.append(args[index])
        elif index % 4 == 3:
            fourths.append(args[index])

    kwargs['a'] = sum(firsts) + kwargs['a']
    kwargs['s'] = kwargs['s'] - sum(seconds)
    if sum(thirds):
        kwargs['d'] = kwargs['d'] / sum(thirds)
    kwargs['m'] = kwargs['m'] * sum(fourths)
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = ""
    for key, value in sorted_result:
        result += f"{key}: {value:.1f}\n"
    return result

print(math_operations(6.0, a=0, s=0, d=5, m=0))