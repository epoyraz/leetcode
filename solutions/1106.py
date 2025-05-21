from collections import deque

class Solution:
    def isEscapePossible(self, blocked, source, target):
        blocked_set = {tuple(p) for p in blocked}
        B = len(blocked)
        if B < 2:
            return True
        # maximum enclosed area ~ B*(B-1)//2
        LIMIT = B * (B - 1) // 2

        def bfs(start, end):
            visited = set()
            q = deque([tuple(start)])
            visited.add(tuple(start))
            while q and len(visited) <= LIMIT:
                x, y = q.popleft()
                if [x, y] == end:
                    return True
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                        if (nx, ny) not in blocked_set and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
            return len(visited) > LIMIT

        # both source and target must not be enclosed
        return bfs(source, target) and bfs(target, source)
