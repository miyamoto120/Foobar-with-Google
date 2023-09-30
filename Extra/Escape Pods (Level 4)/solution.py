def solution(entrances, exits, path):
    flattened = [element for row in path for element in row]
    max_value = max(flattened)
    path.insert(0, [0] * len(path[0]))
    path.append([0] * len(path[0]))
    source = 0
    sink = len(path) - 1
    max_flow = 0
    for i in range(len(path)):
        path[i].insert(0,0)
        path[i].append(0)
    for i in range(len(path[0])):
        for j in entrances:
            if i == j + 1:
                path[0][i] = max_value
    for i in range(len(path)):
        for j in exits:
            if i == j + 1:
                path[i][-1] = max_value
                break
            
    flow = [[0 for _ in range(len(path[0]))] for _ in range(len(path))]
    finish = False
    while True:
        visited = [False] * len(path)
        queue = [source]
        visited[source] = True
        parent = dict()
        while visited[sink] is False:
            if queue == []:
                finish = True
                break
            u = queue.pop(0)
            for v, capacity in enumerate(path[u]):
                if visited[v] is False and capacity - flow[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    continue
        if finish == True:
            break
        s = sink
        path_flow = max_value
        while s!= source:
            path_flow = min(path_flow,path[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            if v != sink and u != source:
                flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

    return(max_flow)