class Solution(object):
    def numDecodings(self, s):
        MOD = 10**9 + 7
        n = len(s)
        dp0, dp1 = 1, 0
        
        if s[0] == '*':
            dp1 = 9
        elif s[0] != '0':
            dp1 = 1
        
        for i in range(1, n):
            temp = dp1
            if s[i] == '*':
                dp1 = 9 * dp1
            elif s[i] != '0':
                dp1 = dp1
            else:
                dp1 = 0
            
            if s[i-1] == '*' and s[i] == '*':
                dp1 += 15 * dp0
            elif s[i-1] == '*':
                if '0' <= s[i] <= '6':
                    dp1 += 2 * dp0
                else:
                    dp1 += dp0
            elif s[i] == '*':
                if s[i-1] == '1':
                    dp1 += 9 * dp0
                elif s[i-1] == '2':
                    dp1 += 6 * dp0
            else:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp1 += dp0
            
            dp1 %= MOD
            dp0 = temp
        
        return dp1
