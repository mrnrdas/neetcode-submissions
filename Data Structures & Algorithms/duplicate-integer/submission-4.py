from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        for val in hash_map.values():
            if val > 1:
                return True
        
        return False