class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # Create a table to store whether s[i:j+1] is a palindrome
        # palindrome[i][j] will be True if s[i...j] is a palindrome
        palindrome = [[False] * n for _ in range(n)]
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            palindrome[i][i] = True
        
        # Check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                palindrome[i][i+1] = True
        
        # Check for substrings of length 3 or more
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and palindrome[i+1][j-1]:
                    palindrome[i][j] = True
        
        # dp[i] represents the minimum cuts needed for s[0:i+1]
        dp = [float('inf')] * n
        
        for i in range(n):
            # If the entire substring s[0:i+1] is a palindrome, no cuts needed
            if palindrome[0][i]:
                dp[i] = 0
            else:
                # Try all possible last cuts
                for j in range(i):
                    if palindrome[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n-1]