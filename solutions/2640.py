class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned_set = set(banned)
        total = count = 0
        for i in xrange(1, n + 1):
            if i in banned_set:
                continue
            if total + i > maxSum:
                break
            total += i
            count += 1
        return count
