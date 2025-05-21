from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes):
        groups = defaultdict(list)
        result = []

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result
