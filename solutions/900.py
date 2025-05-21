class Solution(object):
    def reorderedPowerOf2(self, n):
        from collections import Counter
        target = Counter(str(n))
        for i in range(31):
            if Counter(str(1 << i)) == target:
                return True
        return False
