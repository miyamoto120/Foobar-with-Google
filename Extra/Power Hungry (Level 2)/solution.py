def solution(xs):
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])
    positives = [x for x in xs if x > 0]
    negatives = [x for x in xs if x < 0]
    positive_count = len(positives)
    negative_count = len(negatives)

    if negative_count == 1 and positive_count == 0:
        return str(0)
    if negative_count == 0 and positive_count == 0:
        return str(0)

    max_negative = -1001
    result = 1
    for i in positives:
        result *= i
    for i in negatives:
        result *= i
        max_negative = max(max_negative, i)
    if negative_count % 2 == 1:
        result //= max_negative
    return str(result)