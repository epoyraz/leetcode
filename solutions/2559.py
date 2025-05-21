class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        # nexts[i] will hold lengths of palindrome substrings starting at i with len >= k
        nexts = [[] for _ in range(n)]
        
        # expand odd-length palindromes
        for center in range(n):
            l = center
            r = center
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length >= k:
                    nexts[l].append(length)
                l -= 1
                r += 1
        
        # expand even-length palindromes
        for center in range(n - 1):
            l = center
            r = center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                if length >= k:
                    nexts[l].append(length)
                l -= 1
                r += 1
        
        # dp[i] = max number of palindromic substrings we can pick in s[i:]
        dp = [0] * (n + 1)
        
        # fill dp from end toward 0
        for i in range(n - 1, -1, -1):
            # option 1: skip position i
            best = dp[i + 1]
            # option 2: take any palindrome starting at i
            for length in nexts[i]:
                best = max(best, 1 + dp[i + length])
            dp[i] = best
        
        return dp[0]