class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}

        for i, j in enumerate(nums):
            diff = target - nums[i]

            if diff in hash_table.keys():
                return [hash_table[diff], i]

            hash_table[j] = i

        
        