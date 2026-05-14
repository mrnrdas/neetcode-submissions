from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        for value in hash_map.values():
            if value > 1:
                return True

        return False

