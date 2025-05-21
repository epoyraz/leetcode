class Solution:
    def eliminateMaximum(self, dist, speed):
        times = [(d + s - 1) // s for d, s in zip(dist, speed)]
        times.sort()

        for i, t in enumerate(times):
            if i >= t:
                return i
        return len(dist)
