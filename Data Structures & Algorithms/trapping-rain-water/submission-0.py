class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = [0] * len(height)
        suffix = [0] * len(height)

        max_left = height[0]
        for i in range(1, len(height)):
            max_left = max(max_left, height[i])
            prefix[i] = max_left
        
        max_right = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            max_right = max(max_right, height[i])
            suffix[i] = max_right

        res = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                res += water

        return res

        