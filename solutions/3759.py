import heapq

class Solution(object):
    def findMaxSum(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums1)
        # Pair up (value in nums1, corresponding value in nums2, original index)
        arr = sorted([(nums1[i], nums2[i], i) for i in range(n)], key=lambda x: x[0])
        
        answer = [0] * n
        min_heap = []
        curr_sum = 0
        
        i = 0
        while i < n:
            val = arr[i][0]
            # Process all entries with this same nums1 value
            j = i
            while j < n and arr[j][0] == val:
                _, _, idx = arr[j]
                # Before adding any of this group's nums2, 
                # the heap contains exactly those with nums1 < val
                answer[idx] = curr_sum
                j += 1
            
            # Now include this group's nums2 into our top-k heap
            for t in range(i, j):
                _, w, _ = arr[t]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, w)
                    curr_sum += w
                else:
                    # If this w is larger than the smallest in our heap,
                    # replace to keep the top k largest
                    if min_heap[0] < w:
                        popped = heapq.heapreplace(min_heap, w)
                        curr_sum += w - popped
            
            i = j
        
        return answer
