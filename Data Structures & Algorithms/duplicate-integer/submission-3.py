from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)

        for num in nums:
            if num not in hash_map:
                hash_map[num] += 1
            elif hash_map[num] >= 1:
                return True

        return False
         