class Solution:
    def memLeak(self, memory1, memory2):
        t = 1
        while True:
            if memory1 < t and memory2 < t:
                return [t, memory1, memory2]
            if memory1 >= memory2:
                memory1 -= t
            else:
                memory2 -= t
            t += 1
