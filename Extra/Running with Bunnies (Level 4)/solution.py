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

    def not_in_route(i, route, tocheck):
        result = True
        for j in range(len(route)):
            if i == route[j] and tocheck[i] == True:
                result = False
        return result
    
    def dfs(route, next, remaining_time):
        global path
        current = route[-1]
        remaining_time -= times[current][next]
        for i in visited[current][next]:
            if not_in_route(i, route, tocheck) and i != last:
                route.append(i)
                if times[current][next] <= 0:
                    tocheck.append(False)
                else:
                    tocheck.append(True)
        route.append(next)
        if times[current][next] <= 0:
            tocheck.append(False)
        else:
            tocheck.append(True)
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
                    
    tocheck = [True]
    for i in range(1, n):
        dfs([0], tocheck, i, remaining_time)
    path.sort()
    for i in range(len(path)):
        path[i] -= 1
    return path[1:-1]

s1 = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
s2 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
s3 = [  
[0, 2, 2, -1, 1],
[9, 0, 2, -1, 1], 
[9, 3, 0, -1, 1], 
[9, 3, 2, 0, 1],
[9, 3, 2, -1,  0],
]
s4 = [
[0,9,3,6,4,5,6],
[6,0,6,9,8,1,4],
[6,0,0,4,4,9,6],
[9,6,0,0,7,8,4],
[2,9,6,7,0,2,6],
[9,2,0,2,1,0,6],
[4,1,8,6,4,6,0]
]
print(solution(s1,3))
print(solution(s2,1))
print(solution(s3,3))
print(solution(s4,10))