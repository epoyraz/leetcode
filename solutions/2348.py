class Solution:
    def countTexts(self, pressedKeys):
        mod = 10**9 + 7
        n = len(pressedKeys)
        
        # Precompute dp3[k] = #ways for run of length k with M=3
        #            dp4[k] = #ways for run of length k with M=4
        dp3 = [0] * (n + 1)
        dp4 = [0] * (n + 1)
        dp3[0] = dp4[0] = 1
        
        for k in range(1, n + 1):
            # M = 3
            dp3[k] = dp3[k - 1]
            if k >= 2:
                dp3[k] = (dp3[k] + dp3[k - 2]) % mod
            if k >= 3:
                dp3[k] = (dp3[k] + dp3[k - 3]) % mod
            # M = 4
            dp4[k] = dp4[k - 1]
            if k >= 2:
                dp4[k] = (dp4[k] + dp4[k - 2]) % mod
            if k >= 3:
                dp4[k] = (dp4[k] + dp4[k - 3]) % mod
            if k >= 4:
                dp4[k] = (dp4[k] + dp4[k - 4]) % mod
        
        ans = 1
        i = 0
        while i < n:
            j = i
            # find run of same digit
            while j < n and pressedKeys[j] == pressedKeys[i]:
                j += 1
            length = j - i
            d = pressedKeys[i]
            # choose dp3 or dp4
            if d in {'7', '9'}:
                ans = ans * dp4[length] % mod
            else:
                ans = ans * dp3[length] % mod
            i = j
        
        return ans
