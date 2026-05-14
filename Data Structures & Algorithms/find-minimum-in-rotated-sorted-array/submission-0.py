class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Assign left and right pointer
        left, right = 0, len(nums) - 1

        # While the pointers have not met yet
        while (left < right):

            # If this case is true then list is fully rotated or we have found minimum
            if nums[left] <= nums[right]:
                # Return the minimum
                return nums[left]
            
            # Calculate the mid
            mid = (left + right) // 2

            # If the value at mid is greater than the number at the left pointer
            if (nums[mid] >= nums[left]):
                # Minimum must be to the right of mid
                left = mid + 1
            # Otherwise if the value at mid was less than the value at left pointer
            else:
                # Than the minimum value must be on the left side or equal to the mid
                right = mid
        # After pointers reach we have found the minimum
        return nums[left]
        