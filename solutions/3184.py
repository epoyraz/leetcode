class Solution(object):
    def maxBalancedSubsequenceSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # 1) Compute A[i] = nums[i] - i, and collect for compression
        A = [nums[i] - i for i in range(n)]
        xs = sorted(set(A))
        # map each A[i] to 1-based index in compressed array
        comp = {v: i+1 for i,v in enumerate(xs)}
        m = len(xs)

        # 2) Fenwick tree (1..m) supporting pointâupdate max, prefixâquery max
        class FenwickMax:
            def __init__(self, n):
                self.n = n
                self.fw = [float("-inf")] * (n+1)
            def update(self, i, val):
                # set fw[i] = max(fw[i], val)
                while i <= self.n:
                    if val > self.fw[i]:
                        self.fw[i] = val
                    i += i & -i
            def query(self, i):
                # return max over fw[1..i]
                res = float("-inf")
                while i > 0:
                    if self.fw[i] > res:
                        res = self.fw[i]
                    i -= i & -i
                return res

        fenw = FenwickMax(m)
        ans = float("-inf")

        # 3) DP sweep leftâright
        # dp[i] = w[i] + max(0, max{ dp[j] : j < i, A[j] <= A[i] })
        # we keep in Fenwick at idx=comp[A[j]] the value dp[j]
        for i in range(n):
            idx = comp[A[i]]
            best_prefix = fenw.query(idx)
            # if best_prefix is -inf (no j yet), treat as 0
            if best_prefix < 0:
                best_prefix = 0
            dp_i = best_prefix + nums[i]
            # record dp[i]
            fenw.update(idx, dp_i)
            # track global answer
            if dp_i > ans:
                ans = dp_i

        return ans