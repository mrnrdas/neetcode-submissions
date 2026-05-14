from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = defaultdict(int)

        for num in nums:
            hash_table[num] += 1

        for val in hash_table.values():
            if val > 1:
                return True

        return False

        
