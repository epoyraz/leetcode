from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        
        # Map each value to the list of its indices
        pos = defaultdict(list)
        for i, v in enumerate(arr):
            pos[v].append(i)
        
        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == n - 1:
                    return steps
                
                # Jump to i-1
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    queue.append(i - 1)
                # Jump to i+1
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    queue.append(i + 1)
                # Jump to all other indices with same value
                for j in pos[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)
                # Clear the list to prevent redundant future visits
                pos[arr[i]] = []
            
            steps += 1
        
        return -1
