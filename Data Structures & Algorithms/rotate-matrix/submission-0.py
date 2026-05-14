class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # Save top-left
                top_left = matrix[top][left + i]

                # Move bottom-left to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom-right to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top-right to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Place top-left into top-right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1

