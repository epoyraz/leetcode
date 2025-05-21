from collections import deque

class Solution:
    def continuousSubarrays(self, nums):
        minq = deque()
        maxq = deque()
        l = 0
        total = 0

        for r in range(len(nums)):
            # Maintain monotonic increasing min queue
            while minq and nums[r] < nums[minq[-1]]:
                minq.pop()
            minq.append(r)

            # Maintain monotonic decreasing max queue
            while maxq and nums[r] > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(r)

            # Shrink from left if condition fails
            while nums[maxq[0]] - nums[minq[0]] > 2:
                if minq[0] == l:
                    minq.popleft()
                if maxq[0] == l:
                    maxq.popleft()
                l += 1

            # Add the number of valid subarrays ending at r
            total += r - l + 1

        return total
