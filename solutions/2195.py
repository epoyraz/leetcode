from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        # Queue of (remaining_tickets, person_index)
        q = deque((t, i) for i, t in enumerate(tickets))
        time = 0
        
        while q:
            t, i = q.popleft()
            # One ticket is bought in one second
            time += 1
            t -= 1
            # If this was the kth person and they're done, return time
            if i == k and t == 0:
                return time
            # Otherwise, if they still need more tickets, go to back
            if t > 0:
                q.append((t, i))
        return time  # unreachable, but included for completeness
