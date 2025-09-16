# Last updated: 9/16/2025, 2:17:40 PM
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0
        num_set = set(nums)  # Use a set for fast lookup
        
        # Iterate through the numbers in the array
        for num in nums:
            # Check if both num + diff and num + 2 * diff exist in the set
            if num + diff in num_set and num + 2 * diff in num_set:
                count += 1
        
        return count
