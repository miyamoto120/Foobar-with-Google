def solution(n):
    q = [[0 for _ in range(n + 1)] for _ in range(n - 1)]
    q[0][0] = q [0][1] = 1
    for i in range(1, n - 1):
        for d in range(0, n + 1):
            if d <= i:
                q[i][d] = q[i-1][d]
            else:
                q[i][d] = q[i - 1][d] + q[i - 1][d - i - 1]
    return (q[n - 2][n])