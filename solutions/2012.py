import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)
        m = len(tasks)
        
        # Min-heap of free servers: (weight, index)
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        
        # Min-heap of busy servers: (available_time, weight, index)
        busy = []

        res = []
        time = 0

        for i in range(m):
            time = max(time, i)

            # Free up servers that are done by current time
            while busy and busy[0][0] <= time:
                avail_time, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            # If no free servers, wait until the next one finishes
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    avail_time, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))

            # Assign task
            w, idx = heapq.heappop(free)
            heapq.heappush(busy, (time + tasks[i], w, idx))
            res.append(idx)

        return res
