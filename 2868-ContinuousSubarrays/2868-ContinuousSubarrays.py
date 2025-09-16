# Last updated: 9/16/2025, 2:16:44 PM
class Solution(object):
    def continuousSubarrays(self, nums):
        start = count = 0
        min_deque, max_deque = deque(), deque()

        for end, num in enumerate(nums):
            while max_deque and nums[max_deque[-1]] <= num: max_deque.pop()
            while min_deque and nums[min_deque[-1]] >= num: min_deque.pop()
            max_deque.append(end), min_deque.append(end)
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if max_deque[0] == start: max_deque.popleft()
                if min_deque[0] == start: min_deque.popleft()
                start += 1
            count += end - start + 1

        return count
