from collections import deque

class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0
        
        visited = set()
        queue = deque()
        queue.append((x, 0))  # (current value, steps)

        while queue:
            curr, steps = queue.popleft()
            if curr == y:
                return steps

            if curr in visited:
                continue
            visited.add(curr)

            # Try all four operations:
            # Increment and decrement
            if curr + 1 <= 20000:  # upper bound to avoid explosion
                queue.append((curr + 1, steps + 1))
            if curr - 1 >= 1:
                queue.append((curr - 1, steps + 1))

            # Divide by 5 or 11 if divisible
            if curr % 5 == 0:
                queue.append((curr // 5, steps + 1))
            if curr % 11 == 0:
                queue.append((curr // 11, steps + 1))

        return -1  # Should not reach here
