class Solution(object):
    def checkDistances(self, s, distance):
        first = {}
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if ch in first:
                if i - first[ch] - 1 != distance[idx]:
                    return False
            else:
                first[ch] = i
        return True
