# Last updated: 9/16/2025, 2:16:18 PM
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums
        