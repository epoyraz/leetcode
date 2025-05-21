from collections import Counter

class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        even1 = Counter()
        odd1 = Counter()
        even2 = Counter()
        odd2 = Counter()

        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if i & 1:
                odd1[c1] += 1
                odd2[c2] += 1
            else:
                even1[c1] += 1
                even2[c2] += 1

        return even1 == even2 and odd1 == odd2
