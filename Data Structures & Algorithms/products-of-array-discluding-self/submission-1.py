class Solution:
    def productExceptSelf(self, nums):

        # Initalize the prefix and postfix to 1
        prefix, postfix = 1, 1

        # Get the length of the list
        n = len(nums)

        # Set array all to 1 and have it the same length as the nums list
        res = [1] * n  

        # For i in range length of nums
        for i in range(n):

            # Result at index is equal to prefix
            res[i] = prefix

            # Multiply the prefix by the current array number
            prefix *= nums[i]

        # Loop through the array backwards
        for i in range(n - 1, -1, -1):

            # At the index of the current result multiply the postfix
            res[i] *= postfix

            # At the postfix multiply by the current array number
            postfix *= nums[i]

        # Return result array
        return res
            