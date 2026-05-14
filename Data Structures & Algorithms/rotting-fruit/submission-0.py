from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()
        queue = deque()

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in seen and grid[row][col] == 1

        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    seen.add((row, col))

        if fresh == 0:
            return 0

        time = 0
        while queue:
            current_length = len(queue)
            rotted = False

            for _ in range(current_length):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if isValid(new_row, new_col):
                        seen.add((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))
                        rotted = True
            
            if rotted:
                time += 1

        return time if fresh == 0 else -1
