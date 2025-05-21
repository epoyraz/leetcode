from collections import Counter

class Solution:
    def canReorderDoubled(self, arr):
        count = Counter(arr)
        
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        
        return True
