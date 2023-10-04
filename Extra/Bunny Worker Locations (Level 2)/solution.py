def solution(x, y):
    n = x + y - 2
    return str((n * (n + 1) // 2) + x)