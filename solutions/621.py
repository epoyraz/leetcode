class Solution(object):
    def leastInterval(self, tasks, n):
        from collections import Counter
        counts = Counter(tasks)
        max_count = max(counts.values())
        max_freq = list(counts.values()).count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_freq)
