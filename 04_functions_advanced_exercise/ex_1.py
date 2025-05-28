def stats(*args: int) -> str:
    positives = sum([el for el in args if el > 0])
    negatives = sum([el for el in args if el < 0])
    
    result = f"{negatives}\n{positives}\n"

    if abs(negatives) > positives:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"
    return result

nums = [int(el) for el in input().split()]
print(stats(*nums))
