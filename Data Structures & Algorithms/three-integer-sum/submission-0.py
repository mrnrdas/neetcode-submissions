class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, val in enumerate(nums):
            # index > 0 so we don't get an out of bound error with nums[index - 1]
            if index > 0 and val == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                three_sum = val + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left +=1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
        
