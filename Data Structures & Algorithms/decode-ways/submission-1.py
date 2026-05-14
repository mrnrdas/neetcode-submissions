class Solution:
    def numDecodings(self, s: str) -> int:
        
        # Base case if empty string and initilzie dp dictionary
        dp = {len(s) : 1}

        # DFS helper method
        def dfs(i):
            # If i is in dp than we can return the result already stored
            if i in dp:
                return dp[i]
            # If s[i] = 0 then it cannot be a letter so return 0
            if s[i] == "0":
                return 0

            # Recursively run for single character
            res = dfs(i + 1)

            # Check if valid 2 character
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):  
                # If it is we can add the amount of ways from the 2 character
                res += dfs(i + 2)

            # Store in dp table
            dp[i] = res

            # Return result
            return res

        # Run dfs on 0
        return dfs(0)
        