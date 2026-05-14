# res array initialize
# sort nums so the duplicates are beside eachother
# use enumerate method to get the index and value i am currently at
# check if it is a duplicate or not and past the index
# create two pointers after the left and right
# create a while loop to make sure the left and right do not touch
# if the sum is greater than 0 we can decrement the right pointer
# if the sum is less than 0 we can increment the left pointer
# otherwise if they equal 0 we can add the result to the array
# need to move the pointers so make a while loop to increment the left pointer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, val in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                threeSum = val + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res

