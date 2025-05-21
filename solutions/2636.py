import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        # Pair up nums2 and nums1, sort by nums2 descending
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        min_heap = []
        sum1 = 0
        ans = 0
        
        for val2, val1 in pairs:
            # add this nums1 to heap
            heapq.heappush(min_heap, val1)
            sum1 += val1
            
            # keep only top k nums1 values
            if len(min_heap) > k:
                sum1 -= heapq.heappop(min_heap)
            
            # when we have k elements, compute score
            if len(min_heap) == k:
                ans = max(ans, sum1 * val2)
        
        return ans
