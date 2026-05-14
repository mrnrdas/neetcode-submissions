class Solution:
    def isHappy(self, n: int) -> bool:
        # Slow and fast pointers one starting at n and the other starts at one after n
        slow, fast = n, self.sumOfSquares(n)

        # While the slow and pointer does not reach eachother there is no cycle
        while slow != fast:
            # Fast incremented by 2 step
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            # Slow incremented by 1 step
            slow = self.sumOfSquares(slow)
        # Eventually will meet up and if fast is at 1 than we can return True BUT if not then there was a cycle
        return True if fast == 1 else False

    # Helper method to get the sum of squares
    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output