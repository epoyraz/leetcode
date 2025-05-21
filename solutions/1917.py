import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        def gain(p, t):
            return (p + 1) / (t + 1.0) - p / (t + 0.0)

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p, t), p, t))

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p / float(t) for _, p, t in heap) / len(classes)
