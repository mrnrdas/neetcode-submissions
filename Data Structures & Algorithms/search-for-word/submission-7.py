from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        def isValid(r, c, i, path):
            """Check if the current cell is valid for the current DFS step."""
            return (0 <= r < ROWS and
                    0 <= c < COLS and
                    (r, c) not in path and
                    board[r][c] == word[i])

        def dfs(r, c, i, path):
            """Perform DFS to check if the word can be constructed."""
            if i == len(word):  # All characters are matched
                return True

            if not isValid(r, c, i, path):  # Invalid move
                return False

            # Mark the cell as visited
            path.add((r, c))

            # Explore all possible directions
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1, path):
                    return True

            # Backtrack: Unmark the cell as visited
            path.remove((r, c))
            return False
        
        # Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:  # Potential starting point
                    if dfs(r, c, 0, set()):
                        return True
        
        return False


