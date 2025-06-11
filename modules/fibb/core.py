def create_seq(n):
    seq = [0, 1]

    for _ in range(n-2):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate(seq, number):
    try:
        return seq.index(number)
    except ValueError:
        return f"The number {number} is not in the sequence"