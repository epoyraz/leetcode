class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(1, n):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            next_ugly = min(next2, next3, next5)
            ugly.append(next_ugly)
            
            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1
        
        return ugly[-1]
