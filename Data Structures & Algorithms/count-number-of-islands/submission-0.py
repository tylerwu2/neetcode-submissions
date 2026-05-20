class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        possible_directions = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"

            for direction in possible_directions:
                dfs(r + direction[0], c + direction[1])

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands