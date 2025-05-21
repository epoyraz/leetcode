from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        # Initially, only person 0 and firstPerson know the secret
        known = {0, firstPerson}
        
        # Group meetings by time
        meetings.sort(key=lambda x: x[2])
        i = 0
        m = len(meetings)
        
        while i < m:
            t = meetings[i][2]
            # Build adjacency for this time t
            adj = defaultdict(list)
            j = i
            while j < m and meetings[j][2] == t:
                x, y, _ = meetings[j]
                adj[x].append(y)
                adj[y].append(x)
                j += 1
            
            # Find all participants at this time
            participants = set(adj.keys())
            # BFS from those who already know among participants
            queue = deque([p for p in participants if p in known])
            visited = set(queue)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
            
            # Anyone visited now learns the secret
            known |= visited
            
            # Move to next time block
            i = j
        
        return list(known)
