import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        # Attach friend index to each time and sort by arrival
        events = sorted([(arr, leave, i) for i, (arr, leave) in enumerate(times)],
                        key=lambda x: x[0])
        
        available = []        # min-heap of free chair numbers
        occupied = []         # min-heap of (leave_time, chair)
        next_chair = 0
        
        for arr, leave, idx in events:
            # Free up chairs from friends who have left by time arr
            while occupied and occupied[0][0] <= arr:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)
            
            # Assign the smallest available chair
            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1
            
            # If this is the target friend, we're done
            if idx == targetFriend:
                return chair
            
            # Mark this chair occupied until 'leave'
            heapq.heappush(occupied, (leave, chair))
        
        # Should never reach here if input guarantees targetFriend in times
        return -1
