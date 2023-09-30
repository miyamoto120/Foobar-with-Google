def solution(times, times_limit):
    n = len(times)
    last = n - 1
    visited = [[[] for _ in range(len(times[0]))] for _ in range(len(times))]
    repeat = True
    while repeat:
        repeat = False
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if times[i][j] > times[i][k] + times[k][j]:
                        times[i][j] = times[i][k] + times[k][j]
                        visited[i][j].append(k)
                        repeat = True
    global path
    path = []
    remaining_time = times_limit
    def dfs(route, next, remaining_time):
        global path
        current = route[-1]
        remaining_time -= times[current][next]
        for i in visited[current][next]:
            if i not in route and i != last:
                route.append(i)
        route.append(next)
        if next == n - 1:
            if remaining_time >= 0:
                if len(route) > len(path):
                    path = route[:]
                    return
                if len(route) == len(path):
                    sorted_route = sorted(route)
                    sorted_path = sorted(path)
                    for i in range(len(sorted_route)):
                        if sorted_route[i] < sorted_path[i]:
                            path = route[:]   
                            return
        for i in range(n):
            if i not in route:
                dfs(route,i,remaining_time)
                while route[-1] != next:
                    route.pop()
    for i in range(1, n):
        dfs([0], i, remaining_time)
    path.sort()
    for i in range(len(path)):
        path[i] -= 1
    return path[1:-1]