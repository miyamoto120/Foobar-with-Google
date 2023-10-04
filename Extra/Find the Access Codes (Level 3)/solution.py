def solution(l):
    n = len(l)
    c = [0] * n
    count = 0
    for i in range(n):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]
    return count