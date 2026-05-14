from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_num = len(nums) / 2

        freq = Counter(nums)

        for k, v in freq.items():
            if v > majority_num:
                return k
