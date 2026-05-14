class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        seen = set()
        res = 0

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == 1


        def dfs(row, col):
            seen.add((row, col))
            area = 1

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if isValid(new_row, new_col):
                    area += dfs(new_row, new_col)

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if isValid(row, col):
                    res = max(res, dfs(row, col))

        return res

        