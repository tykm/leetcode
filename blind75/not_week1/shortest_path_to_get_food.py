class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # Find the start location and add it to queue and mark as visited
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    # (row, col, steps)
                    grid[i][j] = "/"
                    q.append((i, j, 0))
        
        # BFS through queue
        while q:
            row, col, steps = q.popleft()
            
            # Go in every direction
            for y, x in directions:
                # newrow, newcol
                nr = row + y
                nc = col + x
                # If tile is OOB or Obstacle or Visited, continue
                if (nr < 0 or nr >= rows or nc < 0 or nc >= cols):
                    continue
                elif grid[nr][nc] in {"X", "/"}:
                    continue
                # Else    
                # Check for Food
                if grid[nr][nc] == "#":
                    return steps + 1
                
                # Mark as visited and add to queue
                grid[nr][nc] = "/"
                q.append((nr, nc, steps + 1))
        return -1