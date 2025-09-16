# Last updated: 9/16/2025, 2:18:18 PM
class Solution(object):
    def countPalindromicSubsequence(self, s):
        left_seen = set()
        right_count = [0] * 26
        
        for char in s:
            right_count[ord(char) - ord('a')] += 1
        
        unique_palindromes = set()
        
        for i, char in enumerate(s):
            right_count[ord(char) - ord('a')] -= 1
            
            for left_char in left_seen:
                if right_count[ord(left_char) - ord('a')] > 0:
                    unique_palindromes.add((left_char, char))
            
            left_seen.add(char)
        
        return len(unique_palindromes)
