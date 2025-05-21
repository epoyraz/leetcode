class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        for ch in set(count_s.keys()).union(count_t.keys()):
            steps += abs(count_s.get(ch, 0) - count_t.get(ch, 0))

        return steps
