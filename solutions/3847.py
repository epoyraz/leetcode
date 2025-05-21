class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # 1) Compute key = (digit_sum, value)
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        # 2) Pair with original index
        arr = [((digit_sum(nums[i]), nums[i]), i) for i in range(n)]
        
        # 3) Sort by key
        arr.sort(key=lambda x: x[0])
        
        # 4) Build P: current index -> target index in sorted array
        P = [0] * n
        for sorted_pos, (_, orig_i) in enumerate(arr):
            P[orig_i] = sorted_pos
        
        # 5) Count cycles in P
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i]:
                continue
            # traverse the cycle
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = P[j]
                cycle_len += 1
            # a cycle of length c needs c-1 swaps
            if cycle_len > 0:
                swaps += cycle_len - 1
        
        return swaps
