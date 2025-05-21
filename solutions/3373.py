class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Precompute primes up to 100
        max_val = 100
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_val + 1, i):
                    is_prime[j] = False
        
        first = -1
        last = -1
        
        for i, x in enumerate(nums):
            if is_prime[x]:
                if first == -1:
                    first = i
                last = i
        
        # If there's at least one prime, last >= first >= 0
        # The maximum distance is last - first (zero if only one prime)
        return last - first
