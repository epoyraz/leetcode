class Solution(object):
    def minimumSteps(self, s):
        steps = 0
        count_ones = 0
        for c in s:
            if c == '1':
                count_ones += 1
            else:
                steps += count_ones
        return steps