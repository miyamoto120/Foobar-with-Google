def solution(src, dest):
    visited = [[False] * 8 for _ in range(8)]
    src_row = src // 8
    src_col = src % 8
    visited[src_row][src_col] = True
    dest_row = dest // 8
    dest_col = dest % 8
    moves = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)
    ]
    queue = [(src_row, src_col, 0)]
    while queue:
        row, col, distance = queue.pop(0)
        if row == dest_row and col == dest_col:
            return distance
        for move_x, move_y in moves:
            new_row, new_col = row + move_x, col + move_y
            if 0 <= new_row < 8 and 0 <= new_col < 8 and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))
    return -1