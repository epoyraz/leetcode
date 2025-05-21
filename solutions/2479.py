import heapq

class Solution(object):
    def mostBooked(self, n, meetings):
        # 1) Sort meetings by their original start time
        meetings.sort(key=lambda x: x[0])
        
        # 2) Minâheap of free rooms (by index)
        free = list(range(n))
        heapq.heapify(free)
        
        # 3) Minâheap of busy rooms: (time_when_free, room_index)
        busy = []
        
        # 4) Count of meetings per room
        count = [0]*n
        
        # 5) Process each meeting
        for start, end in meetings:
            dur = end - start
            
            # Free up any rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                t_free, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                # Assign at its scheduled start
                room = heapq.heappop(free)
                finish = start + dur
            else:
                # No free room now â fast-forward to the earliest free
                t_free, room = heapq.heappop(busy)
                finish = t_free + dur
            
            # Mark room busy until 'finish'
            heapq.heappush(busy, (finish, room))
            count[room] += 1
        
        # 6) Return the room with the highest count (tie â smallest index)
        best = max(range(n), key=lambda i: (count[i], -i))
        return best
