class Solution:
    def distinctSequences(self, n):
        MOD = 10**9 + 7
        
        # Inline gcd
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # allowed[b][a] = True if we can go from previous=a to current=b
        allowed = [[False]*7 for _ in range(7)]
        for a in range(1,7):
            for b in range(1,7):
                if b != a and gcd(a, b) == 1:
                    allowed[b][a] = True
        
        # dp_prev[a][b] = number of sequences ending with [..., b, a]
        dp_prev = [[0]*7 for _ in range(7)]
        # Base case: length=1, we have last=a, second_last=0
        for a in range(1,7):
            dp_prev[a][0] = 1
        
        for _ in range(2, n+1):
            dp_cur = [[0]*7 for _ in range(7)]
            for a in range(1,7):
                for b in range(7):
                    cnt = dp_prev[a][b]
                    if cnt:
                        for c in range(1,7):
                            # c must be coprime with a, different from a and from b
                            if allowed[c][a] and c != b:
                                dp_cur[c][a] = (dp_cur[c][a] + cnt) % MOD
            dp_prev = dp_cur
        
        ans = 0
        for a in range(1,7):
            for b in range(7):
                ans = (ans + dp_prev[a][b]) % MOD
        
        return ans
