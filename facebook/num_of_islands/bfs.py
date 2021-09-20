class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Variables
        visited = set()
        islands = 0
        
        def bfs(i, j):
            # check current already visited:
            if (i, j) in visited or grid[i][j] == '0':
                return
            # mark visited
            visited.add((i, j))
            # visit neighbors if they're in bounds
            neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            for neighbor in neighbors:
                eye, jay = neighbor[0], neighbor[1]
                if eye >= 0 and eye < len(grid) and jay >= 0 and jay < len(grid[eye]):
                    bfs(eye, jay)
        
        # Iterate through land not visited yet
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                land = row[j]     ##same as grid[i,j]
                pos = (i, j)
                if pos not in visited and land == '1':
                    bfs(i, j)
                    islands += 1
        
        return islands
    
    
#  [["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]]
    