from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        queue = deque()

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == 2147483647

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    seen.add((row, col))

        distance = 0
        while queue:
            current_length = len(queue)

            for _ in range(current_length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if isValid(new_row, new_col):
                        seen.add((new_row, new_col))
                        grid[new_row][new_col] = distance + 1
                        queue.append((new_row, new_col))

            distance += 1