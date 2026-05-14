class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize the set
        my_set = set()

        # For num in nums
        for num in nums:

            # If num is found in my_set
            if (num in my_set):

                # We are done we can return True
                return True

            # Otherwise add the num to the set
            my_set.add(num)
        
        # If loop finishes return False
        return False
         