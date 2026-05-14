class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Initialize the hashmap
        my_dict = {}

        # For i in the range of length of nums
        for i in range(len(nums)):

            # Calculate the difference from the target and current number
            diff = target - nums[i]

            # If the difference is in the dictionary keys
            if diff in my_dict.keys():

                # Return the index of the key and the current index
                return [my_dict[diff], i]
            
            # Use the number from the array as the key and the index will be the value
            my_dict[nums[i]] = i
        