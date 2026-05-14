class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        seen = set()
        islands = 0

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == "1"

        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if isValid(new_row, new_col):
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        for row in range(ROWS):
            for col in range(COLS):
                if isValid(row, col):
                    islands += 1
                    dfs(row, col)

        return islands

        