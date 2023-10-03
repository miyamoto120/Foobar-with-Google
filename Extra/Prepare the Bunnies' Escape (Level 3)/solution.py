def solution(map):
    rows = len(map)
    cols = len(map[0])
        
    def bfs(map1):
        # Define directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = [(0, 0, 1)]  # (row, col, path_length)
        visited = set()
        visited.add((0, 0))
        
        while queue:
            row, col, path_length = queue.pop(0)
            
            # Check if reached the bottom right corner
            if row == rows - 1 and col == cols - 1:
                return path_length
            
            # Explore neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within the grid and passable
                if 0 <= new_row < rows and 0 <= new_col < cols and map1[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, path_length + 1))
                    visited.add((new_row, new_col))
        
        # If there is no valid path to the bottom right corner
        return 10000
    
    shortest_length = bfs(map)
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 1:
                map1 = [row[:] for row in map]
                map1[i][j] = 0
                shortest_length = min(bfs(map1), shortest_length)

    return shortest_length