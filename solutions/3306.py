import heapq

class Solution(object):
    def unmarkedSumArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        # Min-heap of all (value, index)
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        
        marked = [False] * n
        unmarked_sum = sum(nums)
        
        answer = []
        for idx, k in queries:
            # 1) Mark the specific index if unmarked
            if not marked[idx]:
                marked[idx] = True
                unmarked_sum -= nums[idx]
            # 2) Mark k smallest unmarked elements
            to_mark = k
            while to_mark > 0 and heap:
                v, i = heapq.heappop(heap)
                if marked[i]:
                    continue
                # mark it
                marked[i] = True
                unmarked_sum -= v
                to_mark -= 1
            # 3) Record current unmarked sum
            answer.append(unmarked_sum)
        
        return answer
