class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Initialize a set with all the numbers without repeating numbers
        numSet = set(nums)

        # Initialize a variable longest to 0
        longest = 0

        # For each number in the set
        for n in numSet:

            # If the number minus one is not in the numSet aka no smaller numbers
            if (n - 1) not in numSet:

                # Length starts at one
                length = 1

                # While the next number is in the set
                while (n + length) in numSet:

                    # We can increase the length
                    length += 1
                
                # Then we can say longest is the max of either the current length of the current longest value
                longest = max(length, longest)
            
        # Then we can return longest
        return longest