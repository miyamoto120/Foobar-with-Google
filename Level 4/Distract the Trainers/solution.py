def solution(banana_list):
    def max_match(edge):
        n = len(edge)
        free_nodes = [i for i in range(n)]
        path = [-1] * n
        next_node = [-1] * n

        while free_nodes:
            root = free_nodes.pop(0)
            queue = []
            visited = [False] * n
            queue.append(root)
            next_free_node = False
            while queue and not next_free_node:
                v = queue.pop(0)
                visited[v] = True
                for w in edge[v]:
                    if next_free_node:
                        break
                    if not visited[w] and path[w] != -1:
                        visited[w] = True
                        next_node[v] = w
                        next_node[w] = v
                        queue.append(path[w])
                    elif w in free_nodes:
                        visited[w] = True
                        next_node[v] = w
                        next_node[w] = v
                        augmenting_path = [w]
                        augmenting_vertex = w
                        free_nodes.remove(w)
                        while True:
                            augmenting_path.append(next_node[augmenting_vertex])
                            if next_node[augmenting_vertex] != root:
                                augmenting_vertex = path[next_node[augmenting_vertex]]
                                augmenting_path.append(augmenting_vertex)
                            else:
                                for vertex in range(0, len(augmenting_path), 2):
                                    path[augmenting_path[vertex]] = augmenting_path[vertex + 1]
                                    path[augmenting_path[vertex + 1]] = augmenting_path[vertex]
                                next_free_node = True
                                break
        max_matching = 0
        for vertex in range(n):
            if path[vertex] != -1:
                max_matching += 1
        return max_matching

    def infinite_battle(a, b):
        total = a + b
        while b:
            a, b = b, a % b
        divide = total / a
        if divide in exponential2:
            return False
        else:
            return True

    exponential2=[1]
    N = len(banana_list)
    for i in range(30): exponential2.append(exponential2[i]*2)

    matching = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if infinite_battle(banana_list[i], banana_list[j]):
                matching[i].append(j)
                matching[j].append(i)

    return N - max_match(matching)