class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, val in enumerate(nums):
            diff = target - nums[index]
            if diff in hash_map.keys():
                return [hash_map[diff], index]
            hash_map[val] = index