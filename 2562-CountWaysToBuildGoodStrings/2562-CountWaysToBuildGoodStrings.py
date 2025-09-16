# Last updated: 9/16/2025, 2:17:15 PM
class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD
    
        return sum(dp[low:high + 1]) % MOD
