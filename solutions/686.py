class Solution(object):
    def repeatedStringMatch(self, a, b):
        repeated = a
        count = 1
        while len(repeated) < len(b):
            repeated += a
            count += 1
        if b in repeated:
            return count
        repeated += a
        if b in repeated:
            return count + 1
        return -1
