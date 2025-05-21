from collections import deque

class Solution:
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        # If start already equals goal (though constraints say start != goal), we'd return 0.
        # Use BFS over x values in [0,1000]
        visited = [False] * 1001
        q = deque()
        q.append((start, 0))
        if 0 <= start <= 1000:
            visited[start] = True

        while q:
            x, steps = q.popleft()
            for v in nums:
                for y in (x + v, x - v, x ^ v):
                    # If we hit the goal, return steps+1 immediately
                    if y == goal:
                        return steps + 1
                    # If y is in [0,1000] and not yet visited, enqueue
                    if 0 <= y <= 1000 and not visited[y]:
                        visited[y] = True
                        q.append((y, steps + 1))
                    # Otherwise, y is out of range and not goal â dead end
        # Exhausted all possibilities without reaching goal
        return -1
