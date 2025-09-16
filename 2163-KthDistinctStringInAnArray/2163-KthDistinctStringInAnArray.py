# Last updated: 9/16/2025, 2:18:16 PM
class Solution(object):
    def kthDistinct(self, arr, k):
        from collections import Counter
        count = Counter(arr)
        distinct_strings = [string for string in arr if count[string] == 1]
        if len(distinct_strings)>=k :
            return distinct_strings[k-1]
        else:
            return ""
        
solution=Solution()
print(solution.kthDistinct(["d", "b", "c", "b", "c", "a"], 2)) 
print(solution.kthDistinct(["aaa", "aa", "a"], 1))         
print(solution.kthDistinct(["a", "b", "a"], 3))