# Last updated: 9/16/2025, 2:16:10 PM
class Solution(object):
    def minimumOperations(self, nums):
        operation=0
        for num in nums:
            remainder= num%3
            if remainder==1:
                operation+=1
            elif remainder==2:
                operation+=1
        return operation