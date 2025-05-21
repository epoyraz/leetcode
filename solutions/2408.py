class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # dp[i] = number of people who learn the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # prefix[i] = dp[1] + dp[2] + ... + dp[i]
        prefix = [0] * (n + 1)
        prefix[1] = 1
        
        for day in range(2, n + 1):
            # j can share on 'day' if:
            #   day - j >= delay  -->  j <= day - delay
            #   day - j < forget  -->  j >  day - forget
            lo = day - forget + 1
            hi = day - delay
            if hi >= 1:
                lo = max(lo, 1)
                dp[day] = (prefix[hi] - prefix[lo - 1]) % MOD
            else:
                dp[day] = 0
            
            prefix[day] = (prefix[day - 1] + dp[day]) % MOD
        
        # People who still remember the secret on day n
        # are those who learned on days j where j + forget > n
        #   j > n - forget
        cutoff = n - forget
        if cutoff >= 1:
            ans = (prefix[n] - prefix[cutoff]) % MOD
        else:
            ans = prefix[n] % MOD
        
        return ans
