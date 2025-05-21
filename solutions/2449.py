from collections import deque

class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        n = len(chargeTimes)
        max_charge_deque = deque()
        sum_running = 0
        l = 0
        ans = 0

        for r in range(n):
            # Add running cost
            sum_running += runningCosts[r]
            # Maintain deque for max charge time
            while max_charge_deque and chargeTimes[r] > max_charge_deque[-1]:
                max_charge_deque.pop()
            max_charge_deque.append(chargeTimes[r])

            # Shrink window while cost exceeds budget
            while l <= r and (max_charge_deque[0] + (r - l + 1) * sum_running) > budget:
                # Remove running cost of leftmost
                sum_running -= runningCosts[l]
                # Pop from deque if it was the max at front
                if max_charge_deque[0] == chargeTimes[l]:
                    max_charge_deque.popleft()
                l += 1

            # Update answer
            ans = max(ans, r - l + 1)

        return ans
