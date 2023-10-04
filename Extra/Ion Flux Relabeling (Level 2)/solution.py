def solution(h, q):
    global parent
    parent = dict()
    global next_node
    next_node = 2 ** h - 1
    parent[next_node] = -1
    def dfs(current,depth):
        global parent
        global next_node
        if depth == 0:
            return
        for i in range(2):
            next_node -= 1
            parent[next_node] = current
            dfs(next_node, depth - 1)
    dfs(next_node, h - 1)
    result = []
    for i in q:
        result.append(parent[i])
    return result