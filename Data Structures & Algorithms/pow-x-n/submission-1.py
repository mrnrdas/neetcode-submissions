class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to calculate power using recursion
        def helper(x, n):
            # Base case 1: if the base 'x' is 0
            if x == 0:
                return 0
            # Base case 2: Any number raised to the power of 0 is 1.
            if n == 0:
                return 1

            # Recursive call: Calculate the result for half the power.
            res = helper(x * x, n // 2)
            
            # If n is odd, multiply the result by 'x' to account for the extra power
            return x * res if n % 2 else res

        # Call helper function with the absolute value of n
        # To handle both positive and negative powers
        res = helper(x, abs(n))

        # If the original n was negative, return the reciprocal of the result
        return res if n >= 0 else 1 / res