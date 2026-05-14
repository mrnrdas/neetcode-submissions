class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def isValid(r, c, index, path):
            """Check if the current position is valid for exploration."""
            return (0 <= r < ROWS and
                    0 <= c < COLS and
                    (r, c) not in path and
                    board[r][c] == word[index])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:  # Start DFS if the first letter matches
                    stack = [(r, c, 0, {(r, c)})]  # (row, column, index, path set)
                    
                    while stack:
                        row, col, index, path = stack.pop()
                        if index == len(word) - 1:
                            return True
                        
                        for dr, dc in directions:
                            new_row, new_col = row + dr, col + dc
                            if isValid(new_row, new_col, index + 1, path):
                                new_path = path.copy()  # Copy the current path
                                new_path.add((new_row, new_col))
                                stack.append((new_row, new_col, index + 1, new_path))
        
        return False

