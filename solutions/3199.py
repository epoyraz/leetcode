class Solution(object):
    def distributeCandies(self, n, limit):
        count = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                k = n - i - j
                if 0 <= k <= limit:
                    count += 1
        return count