# Last updated: 9/16/2025, 2:16:59 PM
class Solution(object):
    def vowelStrings(self, words, queries):
         vowels = {'a', 'e', 'i', 'o', 'u'}
         def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels
         n = len(words)
         prefix_sum = [0] * (n + 1)
         for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_string(words[i]) else 0)
        
         result = []
         for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])
        
         return result