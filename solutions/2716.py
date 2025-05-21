import bisect

class Solution:
    def primeSubOperation(self, nums):
        # Precompute all primes up to max(nums)
        M = max(nums)
        is_prime = [True] * (M+1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(M**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, M+1, i):
                    is_prime[j] = False
        primes = [p for p in range(2, M+1) if is_prime[p]]
        
        prev = -10**18
        # Process each position
        for x in nums:
            # build all possible new values: x itself + x-p for prime p<x
            # (we want them sorted so we can binary-search)
            cand = [x]
            for p in primes:
                if p >= x:
                    break
                cand.append(x - p)
            cand.sort()
            
            # pick the smallest candidate > prev
            j = bisect.bisect_right(cand, prev)
            if j == len(cand):
                return False
            prev = cand[j]
        return True
