class Solution(object):
    def countPairs(self, deliciousness):
        MOD = 10**9 + 7
        from collections import defaultdict
        
        # Precompute powers of two up to 2^21
        powers = [1 << k for k in range(22)]
        
        count = defaultdict(int)
        ans = 0
        
        for val in deliciousness:
            for target in powers:
                need = target - val
                if need in count:
                    ans = (ans + count[need]) % MOD
            count[val] += 1
        
        return ans
