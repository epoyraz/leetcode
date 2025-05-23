from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        r_queue = deque()
        d_queue = deque()
        n = len(senate)
        
        for i, s in enumerate(senate):
            if s == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        
        while r_queue and d_queue:
            r = r_queue.popleft()
            d = d_queue.popleft()
            if r < d:
                r_queue.append(r + n)
            else:
                d_queue.append(d + n)
        
        return "Radiant" if r_queue else "Dire"
