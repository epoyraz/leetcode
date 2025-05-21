class Solution(object):
    def canConstruct(self, s, k):
        from collections import Counter
        if k > len(s):
            return False
        odd_count = sum(1 for count in Counter(s).values() if count % 2 == 1)
        return odd_count <= k
