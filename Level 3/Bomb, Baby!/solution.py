def solution(x, y):
    x = int(x)
    y = int(y)
    if x < y: x, y = y, x
    count = 0
    while y:
        if y == 1: return str(count + x - 1)
        count += x // y - 1
        x, y = y, x % y
        count += 1
        if y == 0: return ("impossible")
    result = str(count + 1)
    return result