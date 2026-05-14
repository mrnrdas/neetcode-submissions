class Solution:
    def climbStairs(self, n: int) -> int:
        # We set up a cache with -1 to indicate we have not explored yet
        cache = [-1] * n

        # DFS helper method
        def dfs(i):
            # Base case if i is equal to n we return 1 for 1 valid path
            if i == n:
                return 1
            # Base case if we overshoot than return 0 for invalid path
            if i > n:
                return 0
            
            # If we have processed i than return the stored value
            if cache[i] != -1:
                return cache[i]
            # Process i with recursive call
            cache[i] = dfs(i + 1) + dfs(i + 2)
            
            # Return value just stored
            return cache[i]

        # Run dfs starting at 0
        return dfs(0)