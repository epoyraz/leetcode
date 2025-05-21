from collections import deque

class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()
        queue = deque([start])

        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            if i in visited:
                continue
            visited.add(i)

            for ni in [i + arr[i], i - arr[i]]:
                if 0 <= ni < n:
                    queue.append(ni)

        return False
