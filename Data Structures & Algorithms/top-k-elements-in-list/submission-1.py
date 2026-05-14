class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Initialize a dictionary to count occurences
        count = defaultdict(int)

        # Count each numbers freqeuncy
        for n in nums:
            count[n] += 1
        
        # Initialize a list where each index represents a frequency
        # With each index holding the numbers that appear with that frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Place each number in the correct index according to its frequency
        for n, c in count.items():
            freq[c].append(n)
        
        # Initialize the result list
        res = []

        # Gather the top k frequency elements
        # Iterate over frequencies from highest to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
