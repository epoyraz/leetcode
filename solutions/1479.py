import heapq

class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            largest = -heapq.heappop(target)
            rest = total - largest
            if largest == 1 or rest == 1:
                return True
            if rest == 0 or largest <= rest:
                return False
            updated = largest % rest
            if updated == 0:
                return False
            total = rest + updated
            heapq.heappush(target, -updated)
