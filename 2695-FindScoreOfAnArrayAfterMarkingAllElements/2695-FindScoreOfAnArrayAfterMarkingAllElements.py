# Last updated: 9/16/2025, 2:16:49 PM
class Solution(object):
    def findScore(self, nums):
        n = len(nums)
        score = 0
        marked = [False] * n
        min_heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(min_heap)

        while min_heap:
            val, i = heapq.heappop(min_heap)
            if marked[i]:
                continue
            score += val
            marked[i] = True
            if i > 0:
                marked[i - 1] = True
            if i < n - 1:
                marked[i + 1] = True

        return score
