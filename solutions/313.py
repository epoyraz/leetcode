import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        heap = []
        for prime in primes:
            heapq.heappush(heap, (prime, prime, 0))
        
        while len(ugly) < n:
            val, prime, idx = heapq.heappop(heap)
            if val != ugly[-1]:
                ugly.append(val)
            heapq.heappush(heap, (prime * ugly[idx + 1], prime, idx + 1))
        
        return ugly[-1]
