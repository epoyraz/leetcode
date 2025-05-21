class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        score = 0
        seen = {}
        max_len = 0

        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1

            if score > 0:
                max_len = i + 1
            elif (score - 1) in seen:
                max_len = max(max_len, i - seen[score - 1])

            if score not in seen:
                seen[score] = i

        return max_len
