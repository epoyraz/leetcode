import heapq

class Solution:
    def findCrossingTime(self, n, k, time):
        waitL = []  # (-efficiency, -index)
        waitR = []  # (-efficiency, -index)
        workL = []  # (available_time, index)
        workR = []  # (available_time, index)

        for i in range(k):
            eff = time[i][0] + time[i][2]
            heapq.heappush(waitL, (-eff, -i))

        curr_time = 0
        boxes_remaining = n
        latest_arrival = 0

        while boxes_remaining > 0 or workR or waitR or workL:
            # Release workers who are done putting or picking
            while workL and workL[0][0] <= curr_time:
                _, i = heapq.heappop(workL)
                eff = time[i][0] + time[i][2]
                heapq.heappush(waitL, (-eff, -i))
            while workR and workR[0][0] <= curr_time:
                _, i = heapq.heappop(workR)
                eff = time[i][0] + time[i][2]
                heapq.heappush(waitR, (-eff, -i))

            if waitR:
                _, i = heapq.heappop(waitR)
                i = -i
                curr_time += time[i][2]  # lefti
                latest_arrival = curr_time  # box has reached left
                heapq.heappush(workL, (curr_time + time[i][3], i))  # putting box
            elif boxes_remaining > 0 and waitL:
                _, i = heapq.heappop(waitL)
                i = -i
                curr_time += time[i][0]  # righti
                heapq.heappush(workR, (curr_time + time[i][1], i))  # picking box
                boxes_remaining -= 1
            else:
                # Jump to the next event time
                next_times = []
                if workL:
                    next_times.append(workL[0][0])
                if workR:
                    next_times.append(workR[0][0])
                if next_times:
                    curr_time = max(curr_time, min(next_times))

        return latest_arrival
