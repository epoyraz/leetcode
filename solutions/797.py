from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        res = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + group_size - 1) // group_size
            res += groups * group_size
        return res
