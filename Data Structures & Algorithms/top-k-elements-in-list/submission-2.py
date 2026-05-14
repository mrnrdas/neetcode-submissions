from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        ans = []

        for num in nums:
            count[num] += 1

        while k > 0:
            curr_max = 0
            max_freq = 0
            for key, val in count.items():
                if val > max_freq:
                    max_freq = val
                    curr_max = key

            count.pop(curr_max)
            ans.append(curr_max)
            k -= 1

        return ans

        
