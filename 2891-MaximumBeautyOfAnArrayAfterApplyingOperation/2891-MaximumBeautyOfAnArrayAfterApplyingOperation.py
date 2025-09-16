# Last updated: 9/16/2025, 2:16:42 PM
class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[right] - nums[left] > 2 * k:
                left += 1
        return len(nums) - left
        