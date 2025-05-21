class Solution:
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute adjacency: allowed[i][j] = True if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0
        allowed = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    a, b = nums[i], nums[j]
                    if a % b == 0 or b % a == 0:
                        allowed[i][j] = True
        
        size = 1 << n
        # dp[mask][last] = number of ways to form permutation using exactly the set bits in mask,
        # ending at index 'last'
        dp = [ [0]*n for _ in range(size) ]
        
        # Base case: single-element permutations
        for i in range(n):
            dp[1<<i][i] = 1
        
        for mask in range(size):
            # try to extend each permutation represented by (mask, last)
            for last in range(n):
                cnt = dp[mask][last]
                if cnt == 0:
                    continue
                # try to append a new element 'nxt'
                rem = (~mask) & (size - 1)
                # iterate over bits in rem
                m = rem
                while m:
                    nxt_bit = m & -m
                    m -= nxt_bit
                    nxt = (nxt_bit.bit_length() - 1)
                    if allowed[last][nxt]:
                        dp[mask | nxt_bit][nxt] = (dp[mask | nxt_bit][nxt] + cnt) % MOD
        
        full = size - 1
        ans = sum(dp[full][i] for i in range(n)) % MOD
        return ans
