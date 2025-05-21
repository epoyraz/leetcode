class Solution(object):
    def minOperations(self, queries):
        import bisect
        
        # Precompute boundaries b[k] = 4^(k-1) for k=1..K
        b = [1]
        while b[-1] <= 10**9:
            b.append(b[-1] * 4)
        K = len(b)  # ~16
        
        # Precompute prefix counts Ck[x] = # a<=x with floor(log4 a)+1 >= k
        # Equivalently, Ck(x) = max(0, x - (4^(k-1)-1))
        def Ck(x, k):
            if x < b[k-1]:
                return 0
            return x - (b[k-1] - 1)
        
        ans = 0
        for l, r in queries:
            # sum of picks = sum_k [Ck(r,k) - Ck(l-1,k)]
            total_picks = 0
            for k in range(1, K+1):
                total_picks += Ck(r, k) - Ck(l-1, k)
            # max single
            # find k s.t. b[k-1]<=r and b[k]>l-1
            max_pick = bisect.bisect_right(b, r)
            # operations
            ops = max(max_pick, (total_picks + 1)//2)
            ans += ops
        
        return ans
