class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[j] = i

        return False