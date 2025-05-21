import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (float(arr[i]) / arr[n-1], i, n-1))
        
        for _ in range(k-1):
            val, i, j = heapq.heappop(heap)
            if j - 1 > i:
                heapq.heappush(heap, (float(arr[i]) / arr[j-1], i, j-1))
        
        val, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
