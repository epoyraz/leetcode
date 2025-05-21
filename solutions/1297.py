from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
