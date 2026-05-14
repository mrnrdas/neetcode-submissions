class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize needed variables for problem
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        seen = set()

        # Create an isValid method to check if current row and col is valid
        def isValid(row, col):
            return 0 <= row < ROW and 0 <= col < COL and grid[row][col] == "1" and (row, col) not in seen

        # Helper dfs method
        def dfs(row, col):
            if not isValid(row, col):
                return

            seen.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        # Loop through the matrix and when running into an island run dfs
        for row in range(ROW):
            for col in range(COL):
                if isValid(row, col):
                    dfs(row, col)
                    islands += 1

        # Return total amount of islands
        return islands
            
            