class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans, i = [], 0
        n = len(nums) * 2

        while n > 0:
            if n == len(nums):
                i = 0
            ans.append(nums[i])
            n -= 1
            i += 1

        return ans
