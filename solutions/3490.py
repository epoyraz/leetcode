class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Count how many evens and odds we have
        cnt_even = 0
        for x in nums:
            if x & 1 == 0:
                cnt_even += 1
        cnt_odd = n - cnt_even
        
        # Case 1: all same parity â adjacent sums are even (0 mod 2)
        max_uniform = max(cnt_even, cnt_odd)
        
        # Case 2: alternating parity â adjacent sums are odd (1 mod 2)
        # Try starting with parity 0, then with parity 1
        # Greedily pick the earliest possible next element of required parity
        alt0 = 0
        cur = 0
        for x in nums:
            if (x & 1) == cur:
                alt0 += 1
                cur ^= 1
        
        alt1 = 0
        cur = 1
        for x in nums:
            if (x & 1) == cur:
                alt1 += 1
                cur ^= 1
        
        return max(max_uniform, alt0, alt1)
