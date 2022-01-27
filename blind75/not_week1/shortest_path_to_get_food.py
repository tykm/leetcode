class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Find starting position
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    q.append((i, j, 0))
                    break
        
        while q:
            row, col, steps = q.popleft()
            for y, x in directions:
                new_row = row + y
                new_col = col + x
                # If new tile is valid
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] in {"#","O"}:
                    # If new tile is food
                    if grid[new_row][new_col] == "#":
                        return steps + 1
                    # Log new tile as visited
                    grid[new_row][new_col] = "/"
                    # Add new tile to bfs queue
                    q.append((new_row, new_col, steps + 1))
        return -1