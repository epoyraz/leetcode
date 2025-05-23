class Solution(object):
    def mostVisited(self, n, rounds):
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        return list(range(1, end + 1)) + list(range(start, n + 1))
