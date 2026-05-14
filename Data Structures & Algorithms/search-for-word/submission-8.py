class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isValid(row, col, index, path):
            return 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in path and board[row][col] == word[index]

        def dfs(row, col, index, path):
            if index == len(word):
                return True

            if not isValid(row, col, index, path):
                return False

            path.add((row, col))

            for dr, dc in directions:
                if dfs(row + dr, col + dc, index + 1, path):
                    return True

            path.remove((row, col))
            return False

        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0, set()):
                        return True

        return False

        