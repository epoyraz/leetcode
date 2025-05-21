class Solution:
    def numPermsDISequence(self, s):
        mod = 10**9 + 7
        # dp[i] = number of ways for the current prefix,
        # where the ârankâ of the last element among used numbers is i.
        dp = [1]  # for an empty pattern, one permutation of length 1
        
        for c in s:
            m = len(dp) + 1
            new_dp = [0] * m
            if c == 'I':
                # build prefix sums of dp
                pre = [0] * (len(dp) + 1)
                for i in range(len(dp)):
                    pre[i+1] = (pre[i] + dp[i]) % mod
                # for 'I', new_dp[j] = sum(dp[0..j-1]) = pre[j]
                for j in range(m):
                    new_dp[j] = pre[j]
            else:  # 'D'
                # build suffix sums of dp
                suf = [0] * (len(dp) + 1)
                for i in range(len(dp)-1, -1, -1):
                    suf[i] = (suf[i+1] + dp[i]) % mod
                # for 'D', new_dp[j] = sum(dp[j..end]) = suf[j]
                for j in range(m):
                    new_dp[j] = suf[j]
            
            dp = new_dp
        
        return sum(dp) % mod
