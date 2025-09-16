# Last updated: 9/16/2025, 2:16:54 PM
class Solution(object):
    def pickGifts(self, gifts, k):
        for _ in range(k):
            max_gift = max(gifts)
            max_index = gifts.index(max_gift)
            gifts[max_index] = int(max_gift ** 0.5)
        return sum(gifts)